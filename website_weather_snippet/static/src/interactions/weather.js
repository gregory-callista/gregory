import {rpc} from "@web/core/network/rpc";
import {registry} from "@web/core/registry";
import {Interaction} from "@web/public/interaction";


class Weather extends Interaction {
    static selector = ".s_weather"

    dynamicSelectors = {
        ...this.dynamicSelectors,
        _locationInput: () => this.locationInputEl
    }

    dynamicContent = {
        ".weather-location-name": {
            "t-out": () => this.locationName?.charAt(0).toUpperCase() + this.locationName?.slice(1)
        },
        ".weather-cards-container": {
            "t-att-class": () => ({"row": !!this.locationName})
        },
        _locationInput: {
            "t-on-change": this.onInputChange,
            "t-att-placeholder": () => this.locationName
        }
    }

    setup() {
        this.locationName = this.el.dataset.locationName;
        this.cardsContainerEl = this.el.querySelector(".weather-cards-container");
        this.locationInputEl = this.el.querySelector("#weather-location-input");
    }

    async willStart() {
        await this.retrieveWeather()
    }

    start() {
        this.updateWeather();
    }

    updateWeather() {
        this.removeChildren(this.cardsContainerEl);

        if (this.weatherData.daily) {
            this.days = this.weatherData.daily.time.map((time, index) => {
                let img;
                const weatherCode = this.weatherData.daily.weathercode[index]

                if (weatherCode === 0) {
                    img = "sun";
                } else if (weatherCode === -1) {
                    img = "sun_hot";
                } else if (weatherCode === -2) {
                    img = "unicorn";
                } else if (weatherCode < 3) {
                    img = "sun_clouds";
                } else if (weatherCode <= 20) {
                    img = "clouds";
                } else {
                    img = "rain";
                }

                return {
                    "date": time,
                    "temp": this.weatherData.daily.temperature_2m_max[index],
                    "img": img

                }
            })

            this.renderAt(
                "website_weather_snippet.s_weather.cards",
                {days: this.days},
                this.cardsContainerEl
            )
        } else {
            this.renderAt(
                "website_weather_snippet.s_weather.not_found",
                {},
                this.cardsContainerEl,
                "afterbegin"
            )
        }
    }

    async onInputChange(ev) {
        this.locationName = ev.currentTarget.value || this.el.dataset.locationName;
        await this.retrieveWeather();
        this.updateWeather();
    }

    async retrieveWeather() {
        this.weatherData = await rpc(
            "/weather_api/get_weather",
            {location: this.locationName}
        );
    }
}

registry.category("public.interactions").add("website_weather_snippet.weather", Weather)

export {Weather}

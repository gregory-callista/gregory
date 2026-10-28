import {Weather} from "./weather"
import { registry } from "@web/core/registry";

const WeatherEdit = (I) => class extends I {
    onInputChange() {}
}

registry.category("public.interactions.edit").add("website_weather_snippet.weather", {
    Interaction: Weather,
    mixin: WeatherEdit
})

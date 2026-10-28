# -*- coding: utf-8 -*-
# Copyright (c) 2026 Callista <https://www.callista.be>
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

{
    "name": "Website Weather Snippet",
    "version": "20.0.1.0.0",
    "summary": "Snippet that shows the weather on your website",
    "author": "Callista BV",
    "website": "https://www.callista.be",
    "license": "LGPL-3",
    "depends": ["website"],
    "data": [
        "views/snippets/s_weather.xml",
        "views/snippets/snippets.xml",
    ],
    "assets": {
        "web.assets_frontend": ["website_weather_snippet/static/src/interactions/**/*"],
        "website.assets_inside_builder_iframe": [
            "website_weather_snippet/static/src/**/*.edit.js"
        ],
    },
    "installable": True,
    "application": False,
    "auto_install": False,
}

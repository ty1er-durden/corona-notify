import argparse
import COVID19Py
import requests

from msteams.messagecard.fact import Fact
from msteams.messagecard.section import Section
from msteams.messagecard.card import MessageCard

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        prog="Corona Notify",
        description="Sends MS Teams notification to webhook with latest COVID-19 stats",
    )
    parser.add_argument(
        "--webhook", required=True, help="MS Teams webhook to send notification to"
    )
    parser.add_argument(
        "--countries",
        nargs="+",
        metavar="CC",
        type=str,
        help="Country codes to include in stats (see https://www.iban.com/country-codes)",
        default=["US", "GB"],
    )

    args = parser.parse_args()

    covid19 = COVID19Py.COVID19()
    data = covid19.getAll()

    countries = args.countries
    url = args.webhook

    filtered = [
        loc
        for loc in data["locations"]
        if loc["country_code"] in countries and loc["province"] == ""
    ]

    # Create Activity Section
    activity_section = (
        Section()
        .activity_group(
            activity_image="https://raw.githubusercontent.com/ty1er-durden/corona-notify/master/images/corona_virus_icon.png",
            activity_title="Bringing you the latest Corona Virus Stats via Python!",
            activity_text="https://github.com/ty1er-durden/corona-notify",
        )
        .build()
    )

    # Add series of stats
    stats_info = Section()
    for loc in filtered:
        stats = f"""{loc["latest"]["confirmed"]} infections\n\n{loc["latest"]["deaths"]} deaths\n"""
        stats_info.fact(Fact(loc["country"].upper(), stats).build())

    # Add activity section to the message card
    message_card = (
        MessageCard()
        .title("COVID-19 Updates")
        .summary("Corona Virus Update")
        .theme_color("FF0000")
        .section(activity_section)
        .section(stats_info.build())
    )

    # Add facts container to the adaptive card and generate the payload message
    payload = message_card.build()

    # Send it to MS Teams
    res = requests.post(url, payload)
    res.raise_for_status()

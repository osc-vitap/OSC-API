from typing import Dict
from dhooks import Embed, Webhook


def send_discord_announcement(webhook_url: str, event: Dict):
    w = Webhook(webhook_url)
    embed = Embed(
        title="📢  " + event["eventName"],
        url=event["eventURL"],
        description=event["eventDescription"],
        color=0x2F3136,
        timestamp="now",
    )

    embed.set_author(
        name="Vijay",
        url="https://github.com/SVijayB",
        icon_url="https://avatars.githubusercontent.com/svijayb",
    )

    embed.add_field(
        name="📍  Event Venue",
        value=event["eventVenue"],
        inline=True,
    )

    data_and_time = event["eventDate"] + " " + event["eventStartTime"]
    embed.add_field(name="⏰  Date and Time", value=data_and_time, inline=True)

    embed.add_field(
        name=":speaker:  Speakers", value=event["eventSpeaker"], inline=False
    )

    embed.add_field(name="📖  Docs", value=event["eventDocumentation"], inline=True)

    embed.set_image(url=event["eventLogo"])

    embed.set_footer(
        text=event["eventCaption"], icon_url="https://i.ibb.co/rFv3nXZ/001-like.png"
    )

    w.send(content="@everyone", embed=embed)

    return True

from typing import List
from dhooks import Embed, Webhook
import traceback


def send_discord_announcement(webhook_url: str, event: List) -> bool:
    try:
        event = event[0]
        w = Webhook(webhook_url)
        embed = Embed(
            title="📢  " + event["eventName"],
            url=event["eventURL"],
            description=event["eventDescription"],
            color=0x2F3136,
            timestamp="now",
        )

        embed.set_author(
            name="Open Source Community: VIT-AP",
            url="https://github.com/Open-Source-Community-VIT-AP",
            icon_url="https://avatars.githubusercontent.com/open-source-community-vit-ap",
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
    except:
        print("Exception occured while trying to send discord announcement...")
        traceback.print_exc()

        return False

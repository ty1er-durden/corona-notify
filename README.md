# Corona Notify

Sends a notification containing the latest COVID-19 stats in MS Teams using an incoming webhook.

## Usage

Create a virtual environment and install the [requirements](requirements.txt):

```bash
python -m pip install -r requirements.txt
```

Schedule a task in **cron** or whatever:

```python corona_notify.py --countries US GB IN SG --webhook https://outlook.office.com/webhook/35b95791-987f-4c09-aa6d-7115c0e35020@04394c60-7431-447d-ae92-9fd0af3dbd0e/IncomingWebhook/b0c1d72aad14428ebe6eb45664eb4e309/78af18d6-7938-44f8-8288-bf14522ed08b```

## Example Message Card

```json
{
    "@context": "https://schema.org/extensions",
    "@type": "MessageCard",
    "sections": [
        {
            "activityImage": "https://raw.githubusercontent.com/ty1er-durden/corona-notify/master/images/corona_virus_icon.png",
            "activityText": "URL: https://github.com/ty1er-durden/corona-notify",
            "activityTitle": "Bringing you the latest Corona Virus Stats via Python"
        },
        {
            "facts": [
                {
                    "name": "INDIA",
                    "value": "Confirmed cases: 657\\n Deaths 12\\n"
                },
                {
                    "name": "SINGAPORE",
                    "value": "Confirmed cases: 631\\n Deaths 2\\n"
                },
                {
                    "name": "UNITED KINGDOM",
                    "value": "Confirmed cases: 9529\\n Deaths 465\\n"
                },
                {
                    "name": "US",
                    "value": "Confirmed cases: 65778\\n Deaths 942\\n"
                }
            ]
        }
    ],
    "summary": "Corona Virus Update",
    "themeColor": "FF0000",
    "title": "COVID-19 Updates"
}
```
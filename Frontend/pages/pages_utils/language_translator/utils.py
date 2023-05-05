import requests


def get_translation_from_hf(input_text, api_url, input_language, output_language):
    ### Make request to  API untill we get a response successfully
    while True:
        try:
            res = requests.post(
                api_url,
                json={
                    "text": input_text,
                    "input_language": input_language,
                    "output_language": output_language,
                },
            )
            # We first check if the response is valid
            translation = res.json()[0]["translation_text"]
            # If the response is valid, we break out of the loop
            if res.status_code == 200:
                break
        except:
            pass

    return translation

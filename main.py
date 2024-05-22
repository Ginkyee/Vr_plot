import json

# Path to your JSON file
json_file_path = 'C:\\Users\\ginky\\Documents\\VR data analysis\\tiktok\\tiktok.json'
# Path to the output text file
output_text_file_path = 'C:\\Users\\ginky\\Documents\\VR data analysis\\tiktok\\transcript.txt'


def extract_transcript(json_path, output_path):
    try:
        # Load the JSON file
        with open(json_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        # Extract the transcript
        transcript = ""
        for result in data.get('results', []):
            for alternative in result.get('alternatives', []):
                transcript += alternative.get('transcript', '') + "\n"

        # Save the transcript to a text file
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(transcript)

        print(f"Transcript successfully saved to {output_path}")

    except Exception as e:
        print(f"An error occurred: {e}")


# Call the function with the paths
extract_transcript(json_file_path, output_text_file_path)

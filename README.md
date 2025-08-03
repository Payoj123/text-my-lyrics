# text-my-lyrics
A Python-based desktop application that allows users to search for song lyrics using the Genius API and send the lyrics URL directly to their phone via SMS using Twilio. Built with Tkinter for the GUI and supports environment variable configuration with python-dotenv.
To use this application:

Create a Twilio account.

Verify your phone number in Twilio (during trial).

Add your TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER, and your verified number as MY_VERIFIED_NUMBER to a .env file.

Create a Twilio account and generate your own Account SID, Auth Token, and Twilio phone number.

Verify your personal phone number with Twilio (required on free tier).

Create a Genius account to get your Genius API access token.

Create your own .env file in the root directory with the following keys:
TWILIO_ACCOUNT_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_PHONE_NUMBER=your_twilio_number
MY_VERIFIED_NUMBER=your_verified_personal_number
GENIUS_ACCESS_TOKEN=your_genius_access_token

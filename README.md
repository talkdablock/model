# model
This repo maintains the LLM application used by the `backend` service for mining blockchain data and providing prompt-engineered response.

## Instructions

### Dependencies
Installing the necessary dependencies are a click away. Simpply run:
```shell
python install -r requirements.txt
```

### OpenAI credentials
At the moment, you'll have to create an OpenAI developer API key before proceeding with any development, testing or other contributions.
You may obtain an OpenAI API Key from https://platform.openai.com/account/api-keys.

Once you have a valid OpenAI API key, you'll want to store it in `.env` file in the project's root directory as shown below:
```shell
$ echo "OPENAI_API_KEY=<YOUR_TOKEN>" >> .env
```

### Dev / QA
While developing or testing, you may:
1. Run the app directly on the host machine using the command:
```shell
uvicorn main:app --host localhost --port 3002
```
2. or, run it as a Docker container:  
Coming Soon™

## License
UNLICENSED

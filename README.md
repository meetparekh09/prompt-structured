# Structured Prompt Experiment

This project demonstrates the power of structured prompting using markdown language to guide Large Language Models (LLMs) in generating well-organized, thoughtful responses. It specifically showcases how using a table of contents and clear section headers can help LLMs break down complex problems and provide structured analysis.

## Motivation

When working with LLMs, the quality and structure of the output heavily depends on how we frame our prompts. This project illustrates how using markdown formatting with clear sections and a table of contents can:

- Guide the LLM through a systematic thinking process
- Ensure all important aspects of a problem are addressed
- Help maintain consistency in response structure
- Make outputs more readable and actionable

The example prompt included analyzes a fictional coffee company's business challenges, demonstrating how structured prompting can lead to better business analysis and decision-making.

## Project Structure 

``` 
├── main.py # Main script to run the LLM interaction
├── prompt.py # Contains the structured markdown prompt
├── Dockerfile # Container configuration
├── Makefile # Automation for docker commands
├── requirements.txt # Python dependencies
└── .env # Environment variables configuration         
```

## Prerequisites

- Docker
- Make (optional, but recommended)
- A local LLM server running on port 1234 (the project is configured to use this by default)

## Setup and Running

1. Clone the repository:

```bash
git clone <repository-url>
cd structured-prompt-experiment
```

2. Configure your environment:
   - The default `.env` configuration is set up for local LLM server:
     ```
     OPENAI_API_KEY=not-needed
     OPENAI_BASE_URL=http://localhost:1234/v1
     OPENAI_CHAT_MODEL=phi-4
     ```
   - Update these variables if you're using a different setup

3. Run using Docker:

Using Make (recommended):
```bash
make build  # Build the Docker image
make run    # Run the container
```

Or using Docker directly:
```bash
docker build -t prompt-structured-app .
docker run --network="host" -v $(PWD):/app -it --rm prompt-structured-app
```

## How It Works

The project demonstrates structured prompting through a business analysis example:

1. **Prompt Structure** (`prompt.py`):
   - Table of contents for clear navigation
   - Introduction section setting context
   - Pros and Cons with expert statements
   - Ideas section for brainstorming
   - Suggestion section for actionable recommendations
   - Appendix for additional resources

2. **Execution** (`main.py`):
   - Loads environment configuration
   - Connects to the LLM service
   - Sends the structured prompt
   - Receives and displays the formatted response

The LLM follows this structure to provide a comprehensive analysis while maintaining the markdown formatting throughout its response.

## Customization

The structured prompt approach can be adapted for various use cases:

1. **Different Analysis Types**:
   - SWOT analysis
   - Market research
   - Technical documentation
   - Project proposals

2. **Prompt Modifications**:
   - Edit `prompt.py` to modify the sections
   - Adjust the structure based on your needs
   - Add or remove sections as required

## Best Practices

When creating structured prompts:

1. Always include a clear table of contents
2. Use consistent heading levels
3. Break down complex topics into manageable sections
4. Include examples or context where helpful
5. End with clear action items or conclusions

## Troubleshooting

Common issues and solutions:

1. **Docker Connection Issues**:
   - If you are running LLM locally, ensure the local LLM server is running
   - Check if port 1234 is accessible
   - Verify network settings in Docker - to make sure Docker has `Enable host networking` enabled.

2. **LLM Response Issues**:
   - Confirm the model name in `.env` matches your server
   - Check the server logs for errors
   - Verify the prompt format is correct

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

Please ensure your changes:
- Follow the existing code style
- Include appropriate documentation
- Add relevant tests if applicable

## License

MIT License

Copyright (c) 2024

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
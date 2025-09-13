# Weather Forecast Chatbot v1.0.0 - AI Agent Instructions

## Architecture Overview
This is a Spanish weather chatbot built with Rasa framework. The architecture follows a modular service pattern:

- **Core Components**: `domain.yml` defines intents/entities/slots, `config.yml` configures SpaCy Spanish NLP + BERT embeddings
- **Custom Actions**: `actions/actions.py` handles form submission using services from `service/` directory
- **Service Layer**: `service/weather.py` (OpenWeatherMap integration), `service/normalization.py` (text→coordinates/dates)
- **Data Flow**: User query → Form collects `date-time` + `address` slots → Custom action fetches weather → Response

## Key Patterns & Conventions

### Spanish Language Processing
- Uses SpaCy `es_core_news_md` model for Spanish NLP
- All responses in `domain.yml` are in Spanish
- NLU training data in `data/nlu.yml` uses Spanish examples
- Date normalization supports: "hoy", "mañana", "pasado mañana" (today, tomorrow, day after)

### Form-Based Conversations
- Weather queries use `weather_form` to collect required slots: `date-time` and `address`
- Rules in `data/rules.yml` activate/submit forms automatically
- Custom action `action_weather_form_submit` processes collected data

### Weather Service Integration
- OpenWeatherMap API via `pyowm` library
- API key loaded from environment: `OWM_KEY` (also accepts `API_KEY`)
- Fetches 8-day forecast, converts to `WeatherCondition(temp_min, temp_max, status)`
- Coordinate resolution: Cities → lat/lon via OpenWeatherMap registry (selects first match)
- Error handling for network issues (ConnectionError, HTTPError, Timeout, TooManyRedirects) in custom actions

### Testing Approach
- Unit tests in `service/test_*.py` using pytest (test coordinates: Shanghai 31.222219, 121.458061)
- Story tests in `tests/test_stories.yml` for conversation flows
- API testing utility in `test_owm.py` for direct OWM API validation
- Run tests: `rasa test` (stories) + `pytest service/` (units)

## Development Workflows

### Training & Running
```bash
rasa train                    # Train NLU + Core models
rasa run                      # Start server (port 5005)
rasa run actions              # Start action server (port 5055)
rasa interactive              # Interactive training mode
```

### Environment Setup
- Install dependencies: `pip install rasa rasa-sdk pyowm python-dotenv spacy`
- Download SpaCy model: `python -m spacy download es_core_news_md`
- Set API keys in `.env`: `OWM_KEY=your_openweather_api_key`
- Web client: `python -m http.server` (serves index.html with showdown.js + github-markdown.css)

### Code Organization
- Keep service logic in `service/` directory (weather.py, normalization.py)
- Custom actions in `actions/actions.py` import from services
- Training data split: `data/nlu.yml` (intents), `data/stories.yml` (flows), `data/rules.yml` (forms)
- Models stored in `models/` with timestamped filenames (e.g., `20240725-065004-atomic-wharf.tar.gz`)

## Common Patterns
- Exception handling in actions: try/catch with user-friendly Spanish error messages
- Slot extraction: `tracker.get_slot("slot_name")`
- Message dispatching: `dispatcher.utter_message(text)` or `dispatcher.utter_message(template="utter_name")`
- Coordinate conversion: Cities → lat/lon via OpenWeatherMap registry (selects first match)
- API error handling: Catches specific exceptions (ConnectionError, HTTPError, Timeout, TooManyRedirects)

## File References
- `domain.yml`: Complete bot capabilities and responses
- `config.yml`: Pipeline configuration (epochs: 100, learning_rate: 0.001)
- `actions/actions.py`: Form submission logic with error handling
- `service/weather.py`: Weather API integration patterns
- `service/normalization.py`: Text processing utilities
- `endpoints.yml`: Action server configuration (localhost:5055)
- `test_owm.py`: Direct API testing utility</content>
<parameter name="filePath">/home/julihocc/rasa/weather/.github/copilot-instructions.md
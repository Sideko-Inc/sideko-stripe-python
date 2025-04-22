import enum


class Environment(enum.Enum):
    """Pre-defined base URLs for the API"""

    PRODUCTION = "https://api.stripe.com"
    MOCK_SERVER = "https://api.sideko.dev/v1/mock/public/stripe/0.1.0"

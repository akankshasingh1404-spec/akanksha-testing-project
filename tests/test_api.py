"""
API Tests — demonstrates:
  • REST API testing with the `requests` library
  • Status code, headers, and response body validation
  • JSON schema validation
  • Independence from UI (faster, more reliable)

Tests against FakeStoreAPI — a public test API.
"""
import pytest
import requests
from jsonschema import validate
from config.config import Config


# ---- JSON Schema for product response ----
PRODUCT_SCHEMA = {
    "type": "object",
    "required": ["id", "title", "price", "category"],
    "properties": {
        "id": {"type": "number"},
        "title": {"type": "string"},
        "price": {"type": "number"},
        "category": {"type": "string"},
        "description": {"type": "string"},
    },
}


class TestProductsAPI:
    """API test suite for the /products endpoint."""

    BASE_URL = Config.API_BASE_URL

    @pytest.mark.smoke
    @pytest.mark.api
    def test_get_all_products_returns_200(self):
        """GET /products should return 200 with a list of products."""
        response = requests.get(f"{self.BASE_URL}/products", timeout=10)

        assert response.status_code == 200
        assert response.headers["Content-Type"].startswith("application/json")

        data = response.json()
        assert isinstance(data, list)
        assert len(data) > 0

    @pytest.mark.regression
    @pytest.mark.api
    def test_get_single_product_schema_validation(self):
        """GET /products/1 response must conform to PRODUCT_SCHEMA."""
        response = requests.get(f"{self.BASE_URL}/products/1", timeout=10)

        assert response.status_code == 200
        validate(instance=response.json(), schema=PRODUCT_SCHEMA)

    @pytest.mark.regression
    @pytest.mark.api
    @pytest.mark.parametrize("product_id", [1, 5, 10, 15])
    def test_get_product_by_valid_id(self, product_id):
        """Data-driven: verify multiple valid product IDs return 200."""
        response = requests.get(f"{self.BASE_URL}/products/{product_id}", timeout=10)
        assert response.status_code == 200
        assert response.json()["id"] == product_id

    @pytest.mark.api
    def test_create_product_returns_201_or_200(self):
        """POST /products should accept a new product payload."""
        payload = {
            "title": "Test Product from QA Framework",
            "price": 19.99,
            "description": "Created via automated API test",
            "category": "electronics",
        }
        response = requests.post(
            f"{self.BASE_URL}/products",
            json=payload,
            timeout=10,
        )
        # FakeStoreAPI returns 200 or 201 on successful create
        assert response.status_code in (200, 201)
        assert response.json()["title"] == payload["title"]

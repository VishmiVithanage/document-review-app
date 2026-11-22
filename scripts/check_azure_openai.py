
from datetime import date
from decimal import Decimal

from app.config import APP_CONFIG, get_settings
from app.documents.schemas import ReviewData, ReviewLineItem


def main() -> None:
    settings = get_settings()
    document = ReviewData(
        vendor_name="Cloud Tools Europe B.V.",
        customer_name=APP_CONFIG.expected_customer_name,
        customer_vat_id=APP_CONFIG.expected_customer_vat_id,
        invoice_number="SAAS-CHECK-001",
        invoice_date=date(2026, 7, 1),
        currency="EUR",
        invoice_total=Decimal("99.00"),
        line_items=[
            ReviewLineItem(
                description="Monthly workflow software subscription",
                quantity=Decimal("1"),
                amount=Decimal("99.00"),
            )
        ],
    )
    print(f"Model: {settings.azure_openai_deployment}")


if __name__ == "__main__":
    main()
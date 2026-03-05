import phonenumbers
from phonenumbers import geocoder, carrier

# Contoh penggunaan nomor (pastikan menyertakan kode negara, misal +62)
phone_number = "+6281234567890"
parsed_number = phonenumbers.parse(phone_number)

# Mendapatkan informasi negara/wilayah (Bukan lokasi presisi saat ini)
location = geocoder.description_for_number(parsed_number, "id")
print(f"Wilayah Registrasi: {location}")

# Mendapatkan informasi provider
service_provider = carrier.name_for_number(parsed_number, "id")
print(f"Provider: {service_provider}")

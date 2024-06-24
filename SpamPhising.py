import requests, datetime, random, string, json

url = "https://chilipepper.io/api/form/submission"
now = datetime.datetime.now()
now = now.strftime("%a, %d %b %Y %H:%M:%S %Z")

password = lambda length=12, include_lower=True, include_upper=True, include_digits=True, include_punctuation=True: "".join(
    random.choice(
        [c for c in string.ascii_lowercase if include_lower]
        + [c for c in string.ascii_uppercase if include_upper]
        + [c for c in string.digits if include_digits]
        + [c for c in string.punctuation if include_punctuation]
    )
    for _ in range(length)
)


def convert_payload_to_json(payload):
  """
  Fungsi untuk mengubah payload biasa menjadi JSON yang valid.

  Args:
    payload: Dictionary yang berisi data payload.

  Returns:
    String yang berisi JSON yang valid.
  """
  try:
    json_data = json.dumps(payload)
  except json.JSONDecodeError:
    pass  # Tidak perlu decode karena sudah format dictionary
  return json_data


payload = {
    "formId": "hot-darkyellow-anaheims-ed492e03-3e8c-44a6-8632-d2c645049af2",
    "data": {
        "4e648f26-5bbf-4df5-a492-c9b85ec5a2ea": "ngentotlah@"+password()+".com",
        "06cd3a35-9646-4e6a-b3d1-a4980d6eb017": "ahhh",
        "839ea2da-03cf-4224-afc7-274bcfb658c1": password(),
        "2c057801-ab26-48c9-bf52-2d5b51457a32": password()
    },
    "updatedAt": now,
    "createdAt": now
}

headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "en-GB,en;q=0.9",
    "cache-control": "no-cache",
    "content-type": "application/json;charset=UTF-8",
    # ... (semua header yang tersisa)
}

# Konversi payload menjadi JSON
json_data = convert_payload_to_json(payload)

# Kirim request POST
response = requests.post(url, headers=headers, data=json_data)

while True:
  if response.status_code == 200:
    # Request berhasil
    print("Request POST berhasil dikirimkan.")
    print(f"Data respons: {response.json()}")
  else:
    # Request gagal
    print(f"Request POST gagal. Status code: {response.status_code}")

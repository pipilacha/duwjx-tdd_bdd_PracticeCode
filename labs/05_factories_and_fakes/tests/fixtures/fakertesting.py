from factory import Faker

providers = ["name", "company", "job", "internet"]

for provider in providers:
    print(f"Provider: {provider}")
    p = Faker(provider)
    for i in range(3):
        print(p.evaluate(instance=None, step=None, extra={"locale": None}))
    print()
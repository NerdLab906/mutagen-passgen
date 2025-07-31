from core.Generator import password_generator
import argparse
import json

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=str, help="Seed for password generation")
    parser.add_argument("--style", type=str, default="classic", help="Style of password (classic, chaos, mystic)")

    args = parser.parse_args()


    if len(args.seed) < 7 or not args.seed.isdigit():
        print("Seed must have only digits and valid length") 
        exit()
    elif len(args.seed) > 16:
        print("Seed limit from 7 to 16")
        exit()

    password = password_generator(args.seed, args.style)
    print(f"\n🔐 Password: {password}")

    with open("data/FE.json", "r") as file:
        data = json.load(file)

    data["counter"] = (data["counter"] + 1) % 4
    with open("data/FE.json", "w") as file:
        json.dump(data, file, indent=4)

if __name__ == "__main__":
    main()
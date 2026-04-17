import json


def load_json(path):
    # Load JSON data from file
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def extract_interfaces(data):
    # Safely extract interface list from nested JSON
    return (
        data.get("imdata", [])
        if isinstance(data, dict)
        else []
    )


def print_interface_status(interfaces):
    # Print formatted interface status table
    print("Interface Status")
    print("=" * 80)
    print(f"{'DN':50} {'Description':20} {'Speed':7} {'MTU':6}")
    print(f"{'-' * 50} {'-' * 20} {'-' * 7} {'-' * 6}")

    for item in interfaces:
        attrs = item.get("l1PhysIf", {}).get("attributes", {})
        dn = attrs.get("dn", "")
        descr = attrs.get("descr", "")
        speed = attrs.get("speed", "inherit")
        mtu = attrs.get("mtu", "")
        print(f"{dn:50} {descr:20} {speed:7} {mtu:6}")


if __name__ == "__main__":
    data = load_json("sample-data.json")
    interfaces = extract_interfaces(data)
    print_interface_status(interfaces)
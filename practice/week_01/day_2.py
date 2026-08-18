# Q1. URL Parameter Cleaner
# Given a raw URL string:

# Python
# url = "///https://api.chai.com/v1/orders/10293.json///"
# Strip all leading and trailing forward slashes (/).

# Extract only the resource ID ("10293") using slicing or string methods.

# Remove the ".json" extension safely using modern Python string methods.


url = "///https://api.chai.com/v1/orders/10293.json///"

stripped_url = url.strip("/")
suffix_removed_url = stripped_url.removesuffix(".json")
final_url = suffix_removed_url[-5:]

print(stripped_url)
print(suffix_removed_url)
print(final_url)
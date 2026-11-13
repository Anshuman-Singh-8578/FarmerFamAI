"""
Legacy reference data from the original Streamlit app (old tips, canned replies, advertised city list).
NOTHING imports this file - Gemini answers all questions now. Keep it for later or delete it.
(The mappings and fallback prices the code still needs live inside main.py.)
"""

# ------------------------------------------------------------------
# REFERENCE ONLY - no longer used by the chatbot
# ------------------------------------------------------------------
FARMING_TIPS = {
    "crops": {
        "wheat": "Wheat grows best in cool, moist climates. Plant in fall or spring. Requires well-drained soil with pH 6.0-7.0.",
        "rice": "Rice needs flooded fields and warm temperatures (20-35°C). Requires clayey soil that retains water well.",
        "corn": "Corn thrives in warm weather with temperatures 21-30°C. Plant after last frost. Needs nitrogen-rich soil.",
        "tomato": "Tomatoes need 6-8 hours of sunlight daily. Plant when soil temperature is above 15°C. Water deeply but infrequently.",
        "potato": "Potatoes prefer cool weather (15-20°C). Plant in loose, acidic soil (pH 5.0-6.0). Hill soil around plants as they grow.",
    },
    "seasons": {
        "spring": "Spring is ideal for planting: tomatoes, peppers, corn, beans, cucumbers, squash, and melons.",
        "summer": "Summer maintenance: Regular watering, pest control, and harvesting early crops. Plant fall vegetables.",
        "fall": "Fall planting: Garlic, onions, winter wheat, cover crops. Harvest summer crops and prepare for winter.",
        "winter": "Winter activities: Plan next season, maintain equipment, indoor seed starting, and cold-frame gardening.",
    },
    "pests": {
        "aphids": "Aphids: Use neem oil spray, introduce ladybugs, or spray with water and mild soap solution.",
        "caterpillars": "Caterpillars: Hand-pick, use Bacillus thuringiensis (Bt), or plant companion flowers to attract predators.",
        "beetles": "Beetles: Hand-pick, use row covers, apply diatomaceous earth, or use neem oil spray.",
        "general": "Pest prevention: Crop rotation, companion planting, beneficial insects, proper spacing, and healthy soil.",
    },
    "soil": {
        "sandy": "Sandy soil: Add compost and organic matter to improve water retention. Good drainage but needs frequent watering.",
        "clay": "Clay soil: Add sand and compost to improve drainage. Rich in nutrients but can become waterlogged.",
        "loamy": "Loamy soil: Ideal for most crops! Balanced mixture of sand, silt, and clay with good drainage and nutrients.",
        "improvement": "Soil improvement: Add compost, use cover crops, practice crop rotation, and test pH regularly.",
    },
}

LEGACY_RESPONSES = {
    "irrigation": (
        "Irrigation Best Practices:\n"
        "- Drip: most efficient, delivers water to roots, saves 30-50% water\n"
        "- Sprinkler: good for large areas, mimics rainfall\n"
        "- Timing: early morning or evening to reduce evaporation\n"
        "- Amount: most crops need 1-2 inches per week\n"
        "- Check soil: water when the top 2 inches are dry"
    ),
    "fertilizer": (
        "Fertilizer Guide:\n"
        "- NPK: N for leaves, P for roots, K for overall health\n"
        "- Organic options: compost, manure, bone meal, fish emulsion\n"
        "- Follow soil test results, don't over-fertilize\n"
        "- Apply before planting and during active growth"
    ),
    "organic": (
        "Organic Farming Tips:\n"
        "- Use compost and manure; rotate crops (3-4 year cycles)\n"
        "- Encourage beneficial insects; use neem or garlic spray\n"
        "- Mulch to retain moisture and suppress weeds\n"
        "- Avoid synthetic pesticides and fertilizers; keep biodiversity"
    ),
    "disease": (
        "Common Plant Diseases & Prevention:\n"
        "- Fungal: improve air circulation, avoid overhead watering, copper fungicides\n"
        "- Bacterial: remove infected plants, rotate crops, resistant varieties\n"
        "- Viral: control insect vectors, remove infected plants immediately\n"
        "- Prevention: proper spacing, clean tools, healthy soil"
    ),
    "harvest": (
        "Harvest Tips:\n"
        "- Harvest in the morning after dew dries\n"
        "- Use sharp, clean tools; handle produce gently\n"
        "- Check crop-specific maturity indicators; store right after harvest"
    ),
}

GENERAL_RESPONSES = [
    "I'm here to help with farming advice! Ask me about crops, weather, market prices, pests, soil, or irrigation.",
    "I can assist with crop selection, pest control, weather updates, market prices, and sustainable farming practices.",
    "Feel free to ask about specific crops, farming techniques, weather, or market prices for any location!",
    "I'm your agricultural assistant! Ask me about planting, harvesting, prices, weather forecasts, or farm management.",
]

ADVERTISED_CITY_LIST = """North: Delhi, Gurgaon, Chandigarh, Ludhiana, Amritsar, Jaipur, Lucknow, Kanpur, Agra
West: Mumbai, Pune, Nagpur, Nashik, Ahmedabad, Surat, Rajkot, Goa
South: Bangalore, Mysore, Mangalore, Chennai, Coimbatore, Madurai, Hyderabad, Vijayawada, Visakhapatnam, Kochi, Thiruvananthapuram
East: Kolkata, Siliguri, Durgapur, Patna, Ranchi, Bhubaneswar, Guwahati
Central: Bhopal, Indore, Raipur"""

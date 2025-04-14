def ask_question(prompt, options=None, allow_multiple=False):
    while True:
        print("\n" + prompt)
        if options:
            for i, opt in enumerate(options, 1):
                print(f"{i}. {opt}")
        try:
            if allow_multiple:
                answer = input("Select all that apply (comma-separated numbers): ")
                selected = [int(i.strip()) for i in answer.split(",")]
                if all(1 <= i <= len(options) for i in selected):
                    return [options[i - 1] for i in selected]
                else:
                    print("⚠️ Please enter valid option numbers.")
            else:
                answer = input("Your answer (number): ")
                selected = int(answer)
                if 1 <= selected <= len(options):
                    return options[selected - 1]
                else:
                    print("⚠️ Please enter a number from the list.")
        except ValueError:
            print("⚠️ Invalid input. Please enter numbers only.")
        except Exception as e:
            print(f"⚠️ Unexpected error: {e}")
            continue

def run_survey():
    score = {
        "relaxed": 0,
        "cultural": 0,
        "active": 0,
        "accessible": 0,
        "balanced": 0
    }

    print("\n🧭 Travel Preferences & Lifestyle Survey")

    ask_question("What is your age group?", [
        "Under 18", "18–25", "26–35", "36–50", "51–65", "65+"
    ])

    group = ask_question("Who do you usually travel with?", [
        "Solo", "Partner", "Family with kids", "Friends", "Group tours", "Caregiver/Assistance required"
    ])
    if group == "Caregiver/Assistance required":
        score["accessible"] += 2

    pace = ask_question("What’s your preferred travel pace?", [
        "Very relaxed", "Relaxed with light walking", "Balanced", "Active", "High-adrenaline"
    ])
    if "relaxed" in pace.lower():
        score["relaxed"] += 2
    elif "balanced" in pace.lower():
        score["balanced"] += 2
    elif "active" in pace.lower() or "adrenaline" in pace.lower():
        score["active"] += 2

    mobility = ask_question("Do you have any mobility limitations or disabilities?", [
        "Yes", "No"
    ])
    if mobility == "Yes":
        score["accessible"] += 3

    accessible_transport = ask_question("Do you require accessible accommodations or transportation?", [
        "Yes", "No", "Prefer but not essential"
    ])
    if accessible_transport != "No":
        score["accessible"] += 2

    comfort_importance = ask_question("How important is comfort and accessibility?", [
        "Extremely important", "Somewhat important", "Not important"
    ])
    if comfort_importance == "Extremely important":
        score["accessible"] += 1
        score["relaxed"] += 1

    ask_question("Do you use any travel aids?", [
        "Wheelchair", "Cane", "Hearing aid", "Vision aid", "None"
    ], allow_multiple=True)

    activities = ask_question("What are your favorite travel activities?", [
        "Museums and history", "Nature walks/hiking", "Water activities",
        "Shopping/city exploring", "Food/wine", "Beach lounging",
        "Adventure sports", "Cultural experiences"
    ], allow_multiple=True)

    if "Museums and history" in activities or "Cultural experiences" in activities:
        score["cultural"] += 2
    if "Food/wine" in activities:
        score["cultural"] += 1
    if "Nature walks/hiking" in activities or "Adventure sports" in activities:
        score["active"] += 2
    if "Beach lounging" in activities:
        score["relaxed"] += 2

    explore_style = ask_question("How do you prefer to explore?", [
        "Guided tours", "Self-paced", "Mix", "Resort/cruise only"
    ])
    if explore_style == "Mix":
        score["balanced"] += 1
    if explore_style == "Resort/cruise only":
        score["relaxed"] += 2

    physical = ask_question("Do you enjoy physical activities on vacation?", [
        "Yes, very much", "Somewhat", "Not really", "Only low-impact"
    ])
    if "very" in physical:
        score["active"] += 2
    elif "low" in physical:
        score["relaxed"] += 1

    outdoors = ask_question("How do you feel about outdoor adventures?", [
        "Love them", "Like in moderation", "Only easy/safe", "Avoid them"
    ])
    if outdoors == "Love them":
        score["active"] += 2
    elif outdoors == "Only easy/safe":
        score["relaxed"] += 1

    wellness = ask_question("Are you interested in wellness or relaxation?", [
        "Spa/meditation", "Yoga/fitness", "Only a little", "Not at all"
    ])
    if "spa" in wellness.lower():
        score["relaxed"] += 2
    if "yoga" in wellness.lower():
        score["balanced"] += 1

    learning = ask_question("Would you enjoy hands-on learning (e.g., cooking)?", [
        "Absolutely", "Maybe a few", "Not interested"
    ])
    if learning == "Absolutely":
        score["cultural"] += 2

    ask_question("What’s your ideal trip duration?", [
        "Weekend getaway", "4–7 days", "1–2 weeks", "More than 2 weeks"
    ])

    accommodation = ask_question("What’s your accommodation preference?", [
        "Luxury", "Mid-range", "Budget", "Unique stays", "Accessibility-first"
    ])
    if "accessibility" in accommodation.lower():
        score["accessible"] += 2

    environment = ask_question("Which environment do you prefer?", [
        "Beach", "Mountains", "Cities", "Countryside", "Variety"
    ])
    if environment == "Beach":
        score["relaxed"] += 1
    elif environment == "Mountains":
        score["active"] += 1

    food = ask_question("How do you feel about trying new foods?", [
        "Love it", "Open to new", "Prefer familiar", "I have restrictions"
    ])
    if food == "Love it":
        score["cultural"] += 2
    elif food == "I have restrictions":
        score["accessible"] += 1

    ask_question("Do you have any travel limitations (e.g., fear of flying)?", [
        "Fear of flying", "Motion sickness", "Altitude", "Health", "None"
    ], allow_multiple=True)

    plan_style = ask_question("Do you prefer scheduled plans or spontaneity?", [
        "Fully scheduled", "Some plans", "Mostly spontaneous", "Totally unplanned"
    ])
    if plan_style == "Some plans":
        score["balanced"] += 1
    if plan_style == "Fully scheduled":
        score["accessible"] += 1

    tech = ask_question("How tech-savvy are you while traveling?", [
        "Use apps a lot", "Moderate use", "Paper maps", "I rely on others"
    ])
    if tech == "I rely on others":
        score["accessible"] += 1

    # Determine top travel type
    top_category = max(score, key=score.get)

    descriptions = {
        "relaxed": "🧘‍♂️ You’re a **Relaxed Explorer** – You value ease, comfort, and light activity. Beaches, resorts, and spa days are your thing!",
        "cultural": "🎭 You’re a **Cultural Enthusiast** – You love history, food, art, and immersive experiences that connect you with local culture.",
        "active": "🥾 You’re an **Active Adventurer** – You live for the outdoors, thrills, and physical activity. Hiking, biking, and exploring all day energize you.",
        "accessible": "♿ You’re an **Accessible Voyager** – You prioritize comfort, accessibility, and thoughtful planning. You enjoy travel that supports your needs and gives you peace of mind.",
        "balanced": "🎒 You’re a **Balanced Traveler** – You enjoy a bit of everything: museums, nature, food, and flexibility. Your perfect trip is a mix of adventure and relaxation."
    }

    print("\n🔎 Based on your answers:")
    print(descriptions[top_category])

if __name__ == "__main__":
    try:
        run_survey()
    except KeyboardInterrupt:
        print("\n⛔ Survey interrupted. Goodbye!")
    except Exception as e:
        print(f"\n⚠️ Something went wrong: {e}")

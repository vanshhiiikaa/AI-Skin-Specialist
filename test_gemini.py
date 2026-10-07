from src.ai_skin_specialist.analyzer import analyze_skin


image_path = "Images/test.jpg"

result = analyze_skin(image_path)

print("\n===== AI SKIN ANALYSIS =====\n")
print(result)

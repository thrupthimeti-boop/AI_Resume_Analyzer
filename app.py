print("=" * 50)
print("           AI RESUME ANALYZER")
print("=" * 50)

name = input("Enter your name: ")
email = input("Enter your email: ")
education = input("Highest Qualification: ")
experience = int(input("Years of Experience: "))
skills = input("Enter your skills (comma separated): ").lower()

required_skills = [
    "python",
    "git",
    "github",
    "html",
    "css",
    "sql"
]

score = 40

report = []
report.append("=" * 50)
report.append("AI RESUME ANALYSIS REPORT")
report.append("=" * 50)
report.append(f"Name: {name}")
report.append(f"Email: {email}")
report.append(f"Education: {education}")
report.append(f"Experience: {experience} year(s)")
report.append("")

print("\n========== SKILL ANALYSIS ==========")

for skill in required_skills:
    if skill in skills:
        print(f"✓ {skill.title()} : Found")
        report.append(f"✓ {skill.title()} : Found")
        score += 10
    else:
        print(f"✗ {skill.title()} : Missing")
        report.append(f"✗ {skill.title()} : Missing")

if experience >= 2:
    score += 10

if score > 100:
    score = 100

print("\nOverall Resume Score:", score, "/100")
report.append(f"\nResume Score: {score}/100")

if score >= 90:
    rating = "Excellent ⭐⭐⭐⭐⭐"
elif score >= 75:
    rating = "Very Good ⭐⭐⭐⭐"
elif score >= 60:
    rating = "Good ⭐⭐⭐"
else:
    rating = "Needs Improvement ⭐⭐"

print("Resume Rating:", rating)
report.append(f"Resume Rating: {rating}")

print("\n========== JOB RECOMMENDATIONS ==========")
report.append("\nJob Recommendations:")

if "python" in skills:
    print("- Python Developer")
    report.append("- Python Developer")

if "html" in skills and "css" in skills:
    print("- Front-End Developer")
    report.append("- Front-End Developer")

if "sql" in skills:
    print("- Database Developer")
    report.append("- Database Developer")

if "git" in skills and "github" in skills:
    print("- Software Engineering Intern")
    report.append("- Software Engineering Intern")

print("\n========== CAREER RECOMMENDATIONS ==========")

if score >= 90:
    print("You are ready for:")
    print("- AI Engineer")
    print("- Software Engineer")
    print("- Full Stack Developer")
    print("- Data Scientist")
elif score >= 75:
    print("You are suitable for:")
    print("- Python Developer")
    print("- Web Developer")
    print("- Front-End Developer")
elif score >= 60:
    print("Recommended roles:")
    print("- Junior Developer")
    print("- Programming Intern")
    print("- Software Trainee")
else:
    print("Improve your resume before applying.")
    print("- Learn Python")
    print("- Build Projects")
    print("- Practice Coding")

print("\n========== SUGGESTIONS ==========")
report.append("\nSuggestions:")

for skill in required_skills:
    if skill not in skills:
        print(f"- Learn {skill.title()}")
        report.append(f"- Learn {skill.title()}")

if experience < 2:
    print("- Gain practical project experience.")
    report.append("- Gain practical project experience.")

print("\n========== FINAL RESULT ==========")

if score >= 80:
    status = "READY FOR JOB APPLICATIONS"
else:
    status = "NEEDS IMPROVEMENT"

print("Resume Status:", status)
report.append(f"\nResume Status: {status}")

report.append("\nThank you for using AI Resume Analyzer!")

with open("resume_report.txt", "w") as file:
    file.write("\n".join(report))

print("\nReport saved successfully as 'resume_report.txt'")
print("Thank you for using AI Resume Analyzer!")
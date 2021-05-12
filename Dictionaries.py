StudentID= {
    "101" : "Bangla",
    "102" : "English",
    "103" : "Math",
    "104" : "CSE"
}

print(StudentID["104"])

print(StudentID.get("101"))

print(StudentID.get("105","Not a valid key"))

print(StudentID.get("103","Not a valid key"))



# bar_chart.py

import matplotlib.pyplot as plt
import numpy
import statistics

subject_data = {
    "Creative Arts": [41, 112, 115, 98, 78, 91, 73, 67, 28, 8, 6, 3, 1, 1, 0, 0],
    "Dance": [19, 54, 41, 25, 27, 21, 4, 10, 3, 0, 0, 0, 0, 0, 0, 0],
    "Drama": [44, 89, 90, 85, 64, 58, 54, 37, 15, 4, 2, 0, 1, 1, 0, 0],
    "Music Explorations": [21, 39, 52, 40, 37, 29, 26, 17, 6, 1, 1, 0, 0, 0, 0, 0],
    "Music Studies": [1, 19, 20, 22, 21, 8, 8, 3, 0, 0, 0, 0, 1, 0, 0, 0],
    "Visual Arts - Art": [69, 116, 123, 112, 123, 92, 99, 97, 41, 8, 7, 1, 1, 0, 0, 0],
    "Visual Arts - Design": [38, 70, 61, 73, 57, 40, 41, 33, 13, 3, 3, 5, 2, 2, 0, 0],
    "Accounting": [21, 54, 55, 68, 45, 49, 51, 30, 12, 11, 3, 3, 3, 1, 1, 0],
    "Business Innovation": [72, 177, 198, 216, 221, 182, 153, 118, 33, 9, 1, 4, 1, 2, 1, 0],
    "Digital Technologies": [19, 52, 44, 42, 31, 22, 26, 30, 15, 2, 1, 0, 0, 1, 1, 0],
    "Information Processing and Publishing": [22, 55, 68, 66, 73, 56, 40, 33, 8, 2, 2, 1, 2, 1, 0, 0],
    "Workplace Practices": [52, 136, 168, 173, 210, 226, 234, 182, 45, 22, 5, 2, 3, 3, 1, 0],
    "Design, Technology and Engineering - Digital Communication Solutions": [50, 111, 123, 90, 90, 90, 66, 72, 21, 2, 1, 1, 0, 0, 0, 0],
    "Design, Technology and Engineering - Industry and Entrepreneurial Solutions": [50, 80, 103, 90, 116, 85, 78, 46, 13, 4, 1, 3, 0, 0, 1, 1],
    "Design, Technology and Engineering - Material Solutions": [30, 105, 173, 175, 173, 162, 194, 156, 32, 6, 7, 3, 5, 4, 3, 0],
    "Design, Technology and Engineering - Robotic and Electronic Systems": [11, 26, 25, 25, 25, 14, 11, 15, 8, 0, 0, 0, 0, 1, 1, 1],
    "Cross-disciplinary Studies: Local Program": [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "Cross-disciplinary Studies": [16, 20, 27, 28, 37, 32, 28, 25, 10, 0, 0, 0, 0, 0, 0, 0],
    "Industry Connections A": [0, 1, 3, 6, 3, 2, 8, 6, 0, 0, 0, 0, 0, 0, 0, 0],
    "Industry Connections B": [0, 0, 0, 0, 1, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    "Integrated Learning A": [65, 136, 169, 154, 218, 212, 202, 182, 57, 10, 7, 3, 4, 1, 0, 0],
    "Integrated Learning B": [66, 47, 50, 67, 90, 92, 86, 69, 13, 6, 2, 1, 0, 0, 0, 0],
    "Humanities and Social Sciences Connections": [0, 0, 11, 16, 43, 41, 57, 70, 15, 3, 0, 1, 0, 0, 0, 0],
    "Interdisciplinary Connections": [1, 7, 8, 15, 41, 83, 100, 112, 21, 4, 2, 0, 0, 0, 0, 0],
    "Practical Connections": [1, 5, 17, 28, 38, 86, 112, 151, 36, 1, 1, 1, 0, 0, 0, 0],
    "STEM Connections": [0, 4, 3, 24, 33, 63, 55, 79, 17, 2, 1, 0, 0, 0, 0, 0],
    "Arts and the Community": [0, 4, 7, 7, 14, 11, 26, 46, 8, 0, 0, 0, 0, 0, 0, 0],
    "Communication and the Community": [0, 1, 0, 4, 3, 13, 9, 16, 4, 2, 0, 0, 1, 0, 0, 0],
    "Foods and the Community": [0, 0, 4, 6, 1, 6, 16, 17, 1, 0, 1, 0, 0, 0, 0, 0],
    "Health, Recreation, and the Community": [0, 2, 5, 6, 10, 7, 12, 38, 7, 0, 1, 0, 0, 1, 0, 0],
    "Science, Technology and the Community": [0, 3, 2, 1, 4, 3, 4, 14, 5, 1, 1, 0, 0, 0, 0, 0],
    "Work and the Community": [0, 0, 3, 6, 23, 19, 37, 42, 7, 0, 0, 1, 0, 0, 0, 0],
    "English": [291, 829, 1180, 1172, 1020, 799, 453, 274, 69, 20, 8, 2, 1, 3, 0, 0],
    "English as an Additional Language": [9, 35, 54, 96, 86, 60, 55, 17, 4, 1, 0, 0, 0, 0, 0, 0],
    "English Literary Studies": [29, 182, 374, 315, 271, 154, 79, 45, 14, 5, 3, 3, 0, 0, 0, 0],
    "Essential English": [18, 100, 234, 315, 369, 360, 327, 185, 32, 5, 4, 2, 2, 0, 0, 0],
    "Child Studies": [66, 158, 222, 199, 198, 142, 87, 67, 21, 9, 2, 3, 2, 0, 2, 0],
    "Food and Hospitality": [66, 172, 263, 224, 230, 223, 175, 111, 42, 4, 2, 5, 0, 0, 0, 0],
    "Health and Wellbeing": [54, 177, 236, 215, 199, 181, 137, 122, 33, 6, 2, 3, 1, 0, 0, 0],
    "Outdoor Education": [45, 87, 129, 112, 138, 112, 111, 99, 41, 11, 4, 4, 2, 1, 1, 0],
    "Physical Education": [67, 160, 186, 188, 199, 209, 200, 174, 78, 11, 4, 2, 4, 3, 0, 0],
    "Aboriginal Studies": [1, 7, 11, 9, 11, 15, 4, 5, 0, 0, 1, 1, 1, 0, 0, 0],
    "Ancient Studies": [20, 51, 57, 48, 43, 51, 44, 35, 12, 4, 0, 0, 0, 0, 0, 0],
    "Economics": [13, 35, 55, 64, 40, 53, 40, 23, 8, 5, 4, 0, 0, 1, 1, 0],
    "Geography": [6, 28, 43, 49, 42, 37, 24, 14, 3, 2, 1, 0, 0, 0, 0, 0],
    "Legal Studies": [14, 55, 86, 116, 81, 110, 81, 54, 34, 17, 8, 1, 3, 4, 1, 0],
    "Media Studies": [15, 45, 37, 43, 39, 39, 19, 10, 5, 3, 2, 0, 0, 0, 0, 0],
    "Modern History": [18, 117, 204, 188, 148, 135, 106, 78, 26, 7, 3, 4, 1, 1, 0, 0],
    "Philosophy": [16, 24, 12, 22, 12, 6, 6, 7, 5, 1, 0, 0, 0, 0, 0, 0],
    "Politics, Power and People": [7, 15, 12, 17, 7, 7, 3, 0, 0, 1, 1, 0, 0, 0, 0, 0],
    "Religion Studies": [12, 25, 30, 27, 15, 11, 3, 10, 9, 2, 0, 0, 0, 0, 0, 0],
    "Society and Culture": [44, 117, 116, 125, 97, 92, 61, 40, 7, 1, 2, 0, 0, 1, 0, 0],
    "Spiritualities, Religion, and Meaning": [12, 23, 23, 19, 8, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    "Tourism": [0, 9, 11, 11, 12, 12, 13, 3, 2, 1, 0, 0, 0, 0, 0, 0],
    "Women's Studies": [9, 22, 20, 27, 28, 17, 9, 15, 4, 1, 1, 0, 0, 1, 0, 0],
    "Chinese (background speakers)": [1, 5, 11, 17, 8, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    "Chinese (continuers)": [8, 20, 23, 11, 9, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "French (continuers)": [3, 20, 22, 9, 11, 6, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "German (beginners)": [0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    "German (continuers)": [4, 8, 13, 8, 8, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "Hindi (continuers)": [1, 2, 5, 3, 4, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "Indonesian (beginners)": [1, 6, 4, 3, 3, 3, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    "Indonesian (continuers)": [1, 10, 3, 4, 1, 2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    "Italian (continuers)": [11, 23, 30, 15, 13, 5, 6, 3, 0, 0, 0, 0, 0, 0, 0, 0],
    "Japanese (beginners)": [0, 0, 2, 3, 1, 8, 1, 3, 0, 0, 0, 0, 0, 0, 0, 0],
    "Japanese (continuers)": [7, 15, 21, 20, 22, 14, 21, 5, 4, 1, 1, 0, 0, 0, 0, 0],
    "Khmer (continuers)": [0, 2, 2, 0, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "Korean (beginners)": [0, 0, 1, 0, 0, 2, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    "Korean (continuers)": [0, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "Spanish (beginners)": [1, 0, 2, 1, 2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    "Spanish (continuers)": [4, 8, 7, 2, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0],
    "Essential Mathematics": [33, 54, 104, 144, 156, 204, 172, 155, 76, 22, 12, 5, 7, 6, 3, 0],
    "General Mathematics": [101, 460, 656, 643, 594, 524, 411, 254, 121, 51, 13, 10, 5, 3, 3, 0],
    "Mathematical Methods": [192, 408, 449, 452, 411, 342, 276, 199, 111, 56, 13, 9, 3, 3, 1, 0],
    "Specialist Mathematics": [58, 130, 120, 162, 136, 130, 111, 70, 43, 25, 3, 1, 2, 1, 0, 0],
    "Agricultural Production": [3, 22, 37, 28, 19, 31, 24, 19, 10, 4, 0, 1, 0, 0, 0, 0],
    "Agricultural Systems": [0, 8, 11, 13, 16, 12, 4, 3, 0, 1, 0, 0, 0, 0, 0, 0],
    "Biology": [74, 273, 339, 461, 406, 336, 246, 191, 97, 36, 15, 7, 5, 3, 0, 0],
    "Chemistry": [51, 211, 318, 357, 283, 193, 157, 125, 67, 19, 13, 4, 1, 4, 1, 0],
    "Earth and Environmental Science": [3, 17, 29, 43, 39, 24, 19, 16, 7, 1, 1, 1, 0, 0, 0, 0],
    "Physics": [48, 141, 224, 282, 250, 178, 147, 91, 43, 14, 5, 3, 3, 0, 0, 0],
    "Psychology": [20, 102, 170, 177, 122, 73, 50, 32, 6, 0, 0, 1, 0, 0, 0, 0],
    "Design and Technology": [27, 80, 122, 120, 111, 103, 94, 67, 34, 5, 3, 1, 2, 0, 0, 0],
    "Digital Solutions": [10, 36, 50, 49, 57, 55, 48, 28, 7, 4, 2, 0, 0, 0, 0, 0],
    "Engineering Studies": [15, 48, 72, 70, 65, 45, 30, 14, 9, 1, 0, 0, 0, 0, 0, 0],
    "Furniture Construction": [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "Metal Engineering": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "Jewellery Manufacture": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "Photographic and Digital Media": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "Textiles and Fashion": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "Visual Communication": [16, 35, 49, 44, 48, 44, 35, 18, 6, 1, 1, 1, 0, 0, 0, 0],
    "Outdoor and Environmental Studies": [13, 62, 90, 70, 72, 61, 41, 26, 12, 4, 2, 1, 1, 0, 0, 0],
    "Sport and Recreation": [9, 40, 52, 42, 49, 43, 29, 21, 6, 3, 2, 0, 0, 0, 0, 0],
    "Algorithmics": [2, 5, 9, 8, 6, 6, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "Applied Computing": [1, 2, 5, 9, 11, 12, 7, 3, 1, 1, 0, 0, 0, 0, 0, 0],
    "Automotive (VET)": [4, 24, 27, 17, 15, 10, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0],
    "Building and Construction (VET)": [10, 37, 52, 43, 45, 32, 17, 10, 2, 0, 0, 0, 0, 0, 0, 0],
    "Community Services (VET)": [2, 6, 11, 13, 6, 4, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    "Dance (VET)": [0, 0, 1, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "Electrotechnology (VET)": [1, 3, 3, 5, 4, 1, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0],
    "Engineering and Related Technologies (VET)": [1, 5, 3, 7, 5, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "Equine Studies (VET)": [0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "Furnishing (VET)": [0, 1, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "Horticulture (VET)": [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "Hospitality (VET)": [3, 18, 35, 37, 22, 19, 10, 6, 3, 0, 0, 0, 0, 0, 0, 0],
    "Information, Digital Media, and Technology (VET)": [8, 33, 46, 47, 39, 31, 18, 10, 5, 1, 0, 0, 0, 0, 0, 0],
    "Music (VET)": [1, 5, 9, 6, 6, 7, 5, 4, 0, 0, 0, 0, 0, 0, 0, 0],
    "Retail (VET)": [1, 1, 3, 5, 2, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    "Screen and Media (VET)": [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "Sport and Recreation (VET)": [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "Textiles, Clothing and Footwear (VET)": [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "Tourism, Travel and Events (VET)": [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "Visual Arts (VET)": [1, 7, 8, 5, 3, 4, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0]
}

grade_bands = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'E+', 'E', 'E-', 'N']

end = False
positive_responses = {"ye", "yes", "yea", "yeah", "y"}
subject = ""

print("--------SACE SUBJECT RESULT 2022--------")
while end == False:
    userinput = input(">> Do you know the specific subject you are looking for? ").lower()
    if userinput in positive_responses:
        while subject != "end":
            subject = input(">> Subject name: ")
            if subject in subject_data:
                def bar_chart(numbers, labels, pos):
                  plt.bar(pos, numbers, color='blue')
                  plt.xticks(ticks=pos, labels=labels)
                  plt.title(f'{subject} Grade Distribution 2022')
                  plt.ylabel('Number of Grades')
                  plt.xlabel('Grade result')
                  plt.show()

                def value_to_grade(data, mean, median, mode):
                    x = data.index(mode)
                    mode = grade_bands[x]
                    y = data.index(median)
                    median = grade_bands[y]
                    closest_num = data[0]  # Initialize with the first number
                    for num in data:
                        if abs(num - mean) < abs(closest_num - mean):
                            closest_num = num
                    z = data.index(closest_num)
                    mean = grade_bands[z]
                    return mean, median, mode

                def remove_values_from_list(the_list, val):
                    return [value for value in the_list if value != val]

                def calculate_statistics(data):
                    data = remove_values_from_list(data, 0)
                    tot_student = sum(data)
                    mean = statistics.mean(data)
                    median = tot_student/2
                    s = 0
                    for i in data:
                        s += i
                        if s > tot_student/2:
                            median = i
                            break
                    mode = max(data)
                    mean, median, mode = value_to_grade(data, mean, median, mode)
                    return mean, median, mode, tot_student

                def display_statistics(subject, mean, median, mode, tot_student):
                    print(f"STATISTICS FOR {subject}")
                    print(f"Total: {tot_student}")
                    print(f"Mean: {mean}")
                    print(f"Median: {median}")
                    print(f"Mode: {mode}")
                    print()
                    
                if __name__ == '__main__':
                    numbers = subject_data[subject]
                    labels = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'E+', 'E', 'E-', 'N']
                    pos = list(range(len(labels)))
                    bar_chart(numbers, labels, pos)
                    mean, median, mode, tot_student = calculate_statistics(subject_data[subject])
                    display_statistics(subject, mean, median, mode, tot_student)
            else:
               print("Subject data not found.")
               print()
               print("Try again.")
               
        

    else:
       print(">> Tsk tsk tsk what are you doing here then")
       print(":/")
       userinput = input("DO you want to end program? ").lower()
       if userinput in positive_responses:
           print("ENDED PROGRAM")
           print("good luck with subject selection")
           end = True




def eligibility(attendenceclasses_held,classes_attended):
    attendence = classes_held/classes_attended*100
    return attendence

if __name__ == "__main__":
    classes_held=int(input("enter number of classes attended"))
    classes_attended=int(input("enter number of classes attended"))
    
    attendence=eligibility(classes_held,classes_attended)
    
    
    if attendence>75:
        print("eligible")
    else:
        print("not eligible")
    

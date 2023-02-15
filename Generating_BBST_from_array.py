gAAAAABfUlP-oqONS-SYK87jMBqMxfW-SfZ-ng2llrzbA5QHcfupFbA5789AgzT2nOPyMPAXZ_rMJLHKNHoHzdnwkyJAHod5Oe_ZfrQmEc_78YOxZgC2GrkVVVJ04OcNi9bkFrQeObe6H9eO6G9CMYE4qCbSbd4KIddug0yT6ROosBwg0lELL1Vfq9Oqe1F1N6oKoKJpCkGrkfepvmY7n0FdZmlNnJRX5ltfRNl3me-JuVahHmXCSF_yt-s9Lf1WiL2r4vaTdDnm0bFYCQPhNlckN4aTsvuMNrIrddRbsveMN3_qA5Z9p33l8AdiRtSESRbfoXOf5rpeK7VbgfaLVxP_pyiRAYNW9uxqMjSy3NaJWZqRKvIj94qXhktC_tv0FIWzL4-S1fERHVbmeLw6KEL50piNRqfi7IFVFCLWW6PZnYw7WcO-pYkUfj924fY5-QYH3IZhQLTJIh-G4BoivQgt0bwi5QnzQA==

def GenerateBBSTArray(a):

    a.sort()
    level = 0
    accum = []
    elements = []
    while len(a) // 2**level > 0:
        accum = [elem for elem in a[len(a) // 2**(level + 1)::(len(a) // 2**level) + 1]]
        elements.extend(accum)
        accum = []
        level += 1
    return elements

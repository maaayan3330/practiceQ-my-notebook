#שאלה 1 – Two Sum, גרסה מורחבת
#נתון מערך של מספרים שלמים nums ומספר target.
#החזירי את כל הזוגות הייחודיים של אינדקסים [i, j] כך ש-nums[i] + nums[j] == target
#אין להשתמש באותו איבר פעמיים.
#אין להחזיר זוגות חופפים (i, j) ו-(j, i) נחשבים אותו דבר.


# גרסה מורחבת - Two Sum - שאלה 1

def cul(nums, target):
    # מילון של מספרים שראינו כבר - המפתח הוא המספר, והערך הוא רשימת אינדקסים
    seen = {}
    # תשמור את התשובות כזוגות (i, j) - בתוך set כדי להימנע מכפולים
    result = set()

    for i, num in enumerate(nums):
        complete = target - num  # המספר שצריך כדי להשלים ל-target
        if complete in seen:
            for j in seen[complete]:
                result.add(tuple(sorted((i, j))))  # לשמור את האינדקסים כסדר עולה
        if num in seen:
            seen[num].append(i)
        else:
            seen[num] = [i]

    return list(result)

# בדיקה:
print("תוצאה:", cul([1, 2, 3, 4], 5))  # אמור להחזיר [(1, 2), (0, 3)]

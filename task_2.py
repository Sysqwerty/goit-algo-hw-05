def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    iterations = 0

    while low <= high:
        mid = (low + high) // 2
        mid_value = arr[mid]

        iterations += 1

        if mid_value < target:
            low = mid + 1
        elif mid_value > target:
            high = mid - 1
        else:
            # Знайдено точний збіг, повертаємо результат
            return iterations, mid_value

    # Якщо не знайдено точний збіг, повертаємо "верхню межу"
    if low < len(arr):
        upper_bound = arr[low]
    else:
        upper_bound = None

    return iterations, upper_bound


# Приклад використання:
if __name__ == "__main__":
    sorted_array = [1.2, 2.3, 3.5, 4.7, 5.8, 7.1, 8.4]
    target_value = 4.5

    iterations, upper_bound = binary_search(sorted_array, target_value)

    print(f"Шукаємо: {target_value}")
    print("Першим елементом є кількість ітерацій, потрібних для знаходження елемента. Другим елементом є 'верхня межа'")
    print(f"Результат: {binary_search(sorted_array, target_value)}")

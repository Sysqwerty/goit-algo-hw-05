# goit-algo-hw-05

[Тема 5. Алгоритми пошуку](https://www.edu.goit.global/uk/learn/13571785/19646173/19656839/training?blockId=19983410)

Проведене порівняння ефективністі алгоритмів пошуку підрядка: Боєра-Мура, Кнута-Морріса-Пратта та Рабіна-Карпа на основі двох текстових файлів.

| Алгоритм                | Стаття 1   | Стаття 2   |
| ----------------------- | ---------- | ---------- |
| Боєра-Мура              | 0.00399    | 0.00342    |
| Кнута-Морріса-Пратта    | 0.00794    | 0.00704    |
| Рабіна-Карпа            | 0.01536    | 0.03606    |

Висновки:
- За результатами обох статей, алгоритм Боєра-Мура виявився найшвидшим серед представлених.

- Алгоритм Кнута-Морріса-Пратта має помірно низькі часові виміри, але трошки повільніший порівняно з Боєра-Муром.

- Рабіна-Карпа виявився найповільнішим за часом серед представлених алгоритмів.

Важливо враховувати, що часові виміри можуть залежати від конкретних умов та обставин, таких як розмір тексту та підрядка, характерістикі обчислювальної системи і т. д. Також важливо враховувати, які саме параметри вимірювалися (наприклад, загальний час пошуку або час на одну операцію).
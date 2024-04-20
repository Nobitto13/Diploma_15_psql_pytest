#Задание 1
#Представь: тебе нужно проверить, отображается ли созданный заказ в базе данных.
#Для этого: выведи список логинов курьеров с количеством их заказов в статусе «В доставке» (поле inDelivery = true).

scooter_rent=SELECT A.login, COUNT(O.id) AS "deliveryCount"
             FROM "Couriers" AS A
             INNER JOIN "Orders" AS O ON A.id = O."courierId"
             WHERE O."inDelivery" = true
             GROUP BY A.login;

#Задание 2
#Ты тестируешь статусы заказов. Нужно убедиться, что в базе данных они записываются корректно.
#Для этого: выведи все трекеры заказов и их статусы.
#Статусы определяются по следующему правилу:
#Если поле finished == true, то вывести статус 2.
#Если поле canсelled == true, то вывести статус -1.
#Если поле inDelivery == true, то вывести статус 1.
#Для остальных случаев вывести 0.

scooter_rent=SELECT track,
             CASE
             WHEN finished = true THEN 2
             WHEN cancelled = true THEN -1
             WHEN "inDelivery" = true THEN 1
             ELSE 0 END AS OrderStatus
             FROM "Orders";

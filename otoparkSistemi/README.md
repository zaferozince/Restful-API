
# OTOPARK SİSTEMİ

## Endpointler

### GET \- /user

Admin kontrolü yapılarak tüm müşteriler getirilir.

#### Örnek Link

`localhost:9696/user?id=1`

Parametre;
1) id


### PUT\- /user

Yeni müşteri kayıtı yapar.

#### Örnek Link

`localhost:9696/user?name=zafer&birthday=22/08/1998&phone_number=5365669775`

Parametreler;
1) name
2) birthday
3) phone_number

### GET\- /users

Kullanıcı id'si ile bilgilerini görüntülemesi için kullanılır.

#### Örnek Link

`localhost:9696/users?id=3`

Parametreler;
1) id

### POST \- /users

Müşteri kullanıcı bilgilerini günceller(Müşteri istediği bilgileri güncelleyebilmektedir).

#### Örnek Link

`localhost:9696/users?id=3&name=zafer&birthday=22/08/1998&phone_number=5365669775`

Parametreler;
1) id
2) name
3) birthday
4) phone_number

### DELETE \- /users

Müşteri kullanıcı bilgilerini silmek için kullanır.


#### Örnek Link

`localhost:9696/users?id=3`

Parametreler;
1) id


### GET\- /login

Müşteri programa girdiğinde ilerlemesi için gereken id'yi alır.

#### Örnek Link

`localhost:9696/login?name=zafer`

Parametreler;
1) name

### GET\- /all

Bütün park durumları getirilir.

#### Örnek Link

`localhost:9696/all`

### GET\- /regs

Müşterinin registration tablosundaki değerlerini alır.

#### Örnek Link

`localhost:9696/regs?id=3`

Parametreler;
1) id

### PUT\- /regs

Müşteri Park etmek için kayıt açar.

#### Örnek Link

`localhost:9696/regs?customer_id=2&park_lot=2`

Parametreler;
1) cutomer_id
2) park_lot

### DELETE\- /regs

Müşteri parkatan çıkması için kullanılır.

#### Örnek Link

`localhost:9696/regs?customer_id=2`

Parametreler;
1) cutomer_id

### GET\- /park

Spesifik bir park alanı çağırılır.

#### Örnek Link

`localhost:9696/park?customer_id=2&id=2`

Parametreler;
1) customer_id
2) id

### POST\- /park

Spesifik bir park alanı günceller.

#### Örnek Link

`localhost:9696/park?customer_id=2&id=2&repletion=0&parkingLot=2`

Parametreler;
1) customer_id
2) id
3) repletion
4) parkingLot

### PUT\- /park

Yeni bir park alanı ekler.

#### Örnek Link

`localhost:9696/park?parkingLot=2`

Parametreler;
1) parkingLot

### DELETE\- /park

Spesifik bir park alanını siler.

#### Örnek Link

`localhost:9696/park?customer_id=2&id=2`

Parametreler;
1) customer_id
2) id





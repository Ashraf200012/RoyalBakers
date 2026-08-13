-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 12, 2026 at 05:58 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.1.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `royalbakers`
--

-- --------------------------------------------------------

--
-- Table structure for table `adminlogin`
--

CREATE TABLE `adminlogin` (
  `id` int(11) NOT NULL,
  `Email` varchar(25) NOT NULL,
  `Password` varchar(10) NOT NULL,
  `username` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `adminlogin`
--

INSERT INTO `adminlogin` (`id`, `Email`, `Password`, `username`) VALUES
(1, 'admin@gmail.com', '396', 'Ashraf');

-- --------------------------------------------------------

--
-- Table structure for table `cart`
--

CREATE TABLE `cart` (
  `id` int(11) NOT NULL,
  `quantity` int(4) NOT NULL,
  `userid` int(11) NOT NULL,
  `proid` int(11) NOT NULL,
  `ProductName` varchar(25) NOT NULL,
  `Price` int(6) NOT NULL,
  `Photo` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `category`
--

CREATE TABLE `category` (
  `id` int(11) NOT NULL,
  `CategoryName` varchar(25) NOT NULL,
  `Description` text NOT NULL,
  `Photo` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `category`
--

INSERT INTO `category` (`id`, `CategoryName`, `Description`, `Photo`) VALUES
(1, 'Cakes', 'A cake is a sweet, baked dessert typically made from flour, sugar, eggs, and fat. Generally, it serves as a symbol of celebration and togetherness and is a staple for special occasions like birthdays and weddings.', 'abc.jpeg'),
(3, 'Breads', 'Bread is a dietary staple food made primarily from cereal flour, water, and salt, typically leavened by yeast or baking powder. It provides essential energy through carbohydrates and vital nutrients, playing a foundational role in diets and global cultures for thousands of years.', 'abc.jpeg'),
(4, 'Pastries', 'In general, a pastry is a delicate baked good made from a dough of flour, water, and high amounts of fat (like butter or shortening). This high fat content creates a light, flaky, or crumbly texture. Pastries can be sweet', 'abc.jpeg'),
(5, 'Donuts', 'A donut generally refers to a small, sweet fried dough confectionery. While traditionally ring-shaped, they come in a wide variety of types and meanings across different contexts.', 'abc.jpeg');

-- --------------------------------------------------------

--
-- Table structure for table `flavour`
--

CREATE TABLE `flavour` (
  `id` int(11) NOT NULL,
  `FlavourName` varchar(20) NOT NULL,
  `Status` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `flavour`
--

INSERT INTO `flavour` (`id`, `FlavourName`, `Status`) VALUES
(1, 'Black Forest', 'Active'),
(2, 'Butterscotch', 'Active'),
(3, 'Rasmalai', 'Active'),
(4, 'Chocolate', 'Active'),
(5, 'Red Velvet', 'Active'),
(6, 'Vanilla', 'Active'),
(7, 'White Bread', 'Active'),
(8, 'Blueberry', 'Active'),
(9, 'Brown Bread', 'Active'),
(10, 'Cheese Bread', 'Active');

-- --------------------------------------------------------

--
-- Table structure for table `ordermaster`
--

CREATE TABLE `ordermaster` (
  `id` int(11) NOT NULL,
  `userid` int(11) NOT NULL,
  `total_amount` int(6) NOT NULL,
  `status` varchar(25) NOT NULL,
  `order_date` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `ordermaster`
--

INSERT INTO `ordermaster` (`id`, `userid`, `total_amount`, `status`, `order_date`) VALUES
(1, 3, 3605, 'Accepted', '2026-08-04 06:03:30'),
(2, 3, 4400, 'Accepted', '2026-08-04 06:09:23'),
(3, 1, 9850, 'Accepted', '2026-08-06 13:14:19'),
(4, 8, 1290, 'Accepted', '2026-08-09 13:21:02');

-- --------------------------------------------------------

--
-- Table structure for table `order_details`
--

CREATE TABLE `order_details` (
  `id` int(11) NOT NULL,
  `order_id` int(11) NOT NULL,
  `proid` int(11) NOT NULL,
  `ProductName` varchar(25) NOT NULL,
  `Photo` text NOT NULL,
  `Price` int(6) NOT NULL,
  `quantity` int(4) NOT NULL,
  `total` int(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `order_details`
--

INSERT INTO `order_details` (`id`, `order_id`, `proid`, `ProductName`, `Photo`, `Price`, `quantity`, `total`) VALUES
(1, 1, 18, 'Customized  Cake', 'abc.jpeg', 1600, 2, 3200),
(2, 1, 7, 'Brown bread', 'abc.jpeg', 45, 9, 405),
(3, 2, 8, 'Butterscotch cake', 'abc.jpeg', 1100, 4, 4400),
(4, 3, 2, 'blueberry donate', 'abc.jpeg', 25, 5, 125),
(5, 3, 6, 'Vanilla pastry', 'abc.jpeg', 35, 10, 350),
(6, 3, 11, 'Chocolate Wedding cake', 'abc.jpeg', 1875, 5, 9375),
(7, 4, 22, 'Rasmalai pastry', 'abc.jpeg', 44, 10, 440),
(8, 4, 5, 'Red velvet cake', 'abc.jpeg', 850, 1, 850);

-- --------------------------------------------------------

--
-- Table structure for table `product`
--

CREATE TABLE `product` (
  `id` int(11) NOT NULL,
  `ProductName` varchar(30) NOT NULL,
  `CategoryName` varchar(25) NOT NULL,
  `FlavorName` varchar(25) NOT NULL,
  `UnitName` varchar(4) NOT NULL,
  `Price` varchar(6) NOT NULL,
  `Description` text NOT NULL,
  `Photo` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `product`
--

INSERT INTO `product` (`id`, `ProductName`, `CategoryName`, `FlavorName`, `UnitName`, `Price`, `Description`, `Photo`) VALUES
(1, 'Black Forest cake', 'Cakes', 'Black Forest', 'kg', '900', 'Black Forest cake is a famous German dessert featuring layers of chocolate sponge cake, whipped cream, and cherries, traditionally soaked with a cherry brandy liqueur called Kirschwasser.', 'abc.jpeg'),
(2, 'blueberry donate', 'Donuts', 'Blueberry', 'NOS', '25', 'A blueberry donate cake typically refers to a homemade or bakery-bought blueberry cake that is prepared specifically for a charity bake sale, a community donation drive, or gifted to a friend, neighbor, or local organization.', 'abc.jpeg'),
(3, 'white bread', 'Breads', 'White Bread', 'NOS', '45', 'White bread is a soft, light-colored bread made from wheat flour often called maida that has had the nutrient-rich bran and germ removed during milling. It is prized for its long shelf life, fluffy texture, and versatility, though it is lower in fiber than whole grain options.', 'abc.jpeg'),
(4, 'Cheese bread', 'Breads', 'Cheese Bread', 'NOS', '75', 'Cheese bread is a savory baked good loaded or topped with cheese. It comes in various forms worldwide, ranging from classic loaves filled with melted cheddar', 'abc.jpeg'),
(5, 'Red velvet cake', 'Cakes', 'Red Velvet', 'kg', '850', 'Red velvet cake is a classic American dessert featuring a distinctive deep red sponge and a bright white cream cheese frosting. It has a unique flavor profile a blend of mild cocoa and a distinct tanginess???paired with a very soft, smooth, and velvety texture.', 'abc.jpeg'),
(6, 'Vanilla pastry', 'Pastries', 'Vanilla', 'NOS', '35', 'Vanilla Pastry Cream the rich, velvety custard filling used in many desserts or a Vanilla Slice a classic Australian European dessert with vanilla custard sandwiched between puff pastry', 'abc.jpeg'),
(7, 'Brown bread', 'Breads', 'Brown Bread', 'NOS', '45', 'Brown bread is a general term for bread made with whole grain or unrefined flours, giving it a darker color and higher nutritional value than white bread. Brown bread is a general term for bread made with whole grain or unrefined flours, giving it a darker color and higher nutritional value than white bread.', 'abc.jpeg'),
(8, 'Butterscotch cake', 'Cakes', 'Butterscotch', 'kg', '1100', 'A butterscotch cake is a rich, indulgent dessert flavored with buttery toffee and caramelized sugar. It typically features layers of soft sponge cake soaked in butterscotch or caramel syrup, frosted with creamy butterscotch buttercream, and decorated with crunchy praline or butterscotch chips.', 'abc.jpeg'),
(9, 'Rasmalai Donut', 'Donuts', 'Rasmalai', 'NOS', '65', 'A Rasmalai Donut Cake is an innovative fusion dessert that combines the rich, aromatic flavors of the traditional Indian sweet Rasmalai with the soft, fluffy texture of a donut or cake. It typically features a cardamom and saffron sponge soaked in sweet milk, topped with frosting, and garnished with pistachios and rose petals.', 'abc.jpeg'),
(10, 'Blueberry cake', 'Cakes', 'Blueberry', 'kg', '720', 'A blueberry cake is a moist dessert made with a soft, vanilla, or lemon scented sponge batter folded with juicy fresh or frozen blueberries. It is typically served as a simple, crackly-topped single-layer treat for breakfast or as an elegant frosted layer cake for birthdays and celebrations', 'abc.jpeg'),
(11, 'Chocolate Wedding cake', 'Cakes', 'Chocolate', 'kg', '1875', 'A chocolate wedding cake is a decadent, rich alternative to traditional vanilla or fruitcake. Featuring moist, dense chocolate sponge layers, it is usually filled and frosted with rich chocolate ganache or buttercream. These cakes can be designed in classic multiple tiers or a single-tier presentation', 'abc.jpeg'),
(12, 'Chocolate Donut', 'Donuts', 'Chocolate', 'NOS', '25', 'A chocolate donut is a sweet, fried or baked pastry made with cocoa powder in the dough. They come in two primary varieties: cake donuts dense and crumbly or yeast donuts fluffy and airy They are typically topped with a chocolate glaze, icing, or sprinkles', 'abc.jpeg'),
(13, 'Black Forest donut', 'Donuts', 'Black Forest', 'NOS', '85', 'A Black Forest donut is a rich, decadent treat inspired by the famous German Black Forest Cake. It translates the classic desserts flavor profile into a handheld pastry typically featuring a chocolate donut base a sweet cherry or tart compote filling and a topping of whipped cream and dark chocolate shavings', 'abc.jpeg'),
(14, 'Baby shower red velvet Cake', 'Cakes', 'None', 'kg', '1430', 'A baby shower red velvet cake is KabhiB. It is traditionally frosted and filled with rich, tangy cream cheese buttercream. For baby showers, these cakes are playfully decorated using pink blue or gender-neutral fondants, ribbons, and baby-themed toppers.', 'abc.jpeg'),
(15, 'Rasmalai Engagement Cake', 'Cakes', 'Rasmalai', 'kg', '1700', 'A Rasmalai Engagement Cake is a fusion dessert that combines the rich,traditional flavors of the beloved Indian sweet Rasmalai with a modern western-style layered cake. It serves as a popular culturally rich centerpiece for engagement ceremonies', 'abc.jpeg'),
(16, 'Spider-Man cake', 'Cakes', 'Blueberry', 'kg', '1900', 'A Spider-Man cake is a themed dessert decorated to resemble the famous Marvel superhero. It is highly popular for childrens birthdays and is typically designed with his iconic red and blue suit, black spider web piping, the spider emblem, or 3D character toppers.', 'abc.jpeg'),
(17, 'Motu Patlu Cartoon Cake', 'Cakes', 'Vanilla', 'kg', '1299', 'A Motu Patlu Cartoon Cake is a custom-themed birthday or celebration cake featuring the beloved characters from the popular Indian animated television series Motu Patlu. It is a massive hit for kids birthdays across India.', 'abc.jpeg'),
(18, 'Customized  Cake', 'Cakes', 'Chocolate', 'kg', '1600', 'A customized or custom cake is a dessert designed and baked specifically for an individual or event, going beyond standard off the shelf bakery options.', 'abc.jpeg'),
(19, 'Donut  combo', 'Donuts', 'Butterscotch', 'NOS', '55', 'In the context of food, a \"donut combo\" is a menu pairing that combines a donut with a complementary beverage like a fresh coffee or tea or a complementary savory snack like a samosa or sandwichIt offers a balanced sweet-and-savory or sweet and bitter flavor profile for a complete meal or snack', 'abc.jpeg'),
(20, 'Butterscotch Pastry', 'Pastries', 'Butterscotch', 'NOS', '20', 'A butterscotch pastry is a rich dessert featuring layers of moist vanilla or caramel infused sponge cake. It is soaked in sweet caramel syrup filled with smooth whipped butterscotch cream, and generously garnished with crunchy praline bits', 'abc.jpeg'),
(21, 'Red Velvet Pastry', 'Pastries', 'Red Velvet', 'NOS', '70', 'A red velvet pastry is a striking, crimson colored dessert featuring a soft, velvety sponge cake with a subtle cocoa and vanilla flavor. It is traditionally layered and topped with rich, tangy cream cheese frosting. Its signature soft crumb and flavor come from a chemical reaction between buttermilk, vinegar, and cocoa powder', 'abc.jpeg'),
(22, 'Rasmalai pastry', 'Pastries', 'Rasmalai', 'NOS', '44', 'A Rasmalai pastry is a fusion dessert that combines the rich, traditional flavors of the beloved Indian Rasmalai spongy cheese dumplings soaked in cardamom and saffron-infused milk with the light, layered structure of a Western-style bakery pastry or cake.', 'abc.jpeg'),
(23, 'Milk brown bread', 'Breads', 'Brown Bread', 'NOS', '54', 'Milk brown bread is a soft, enriched loaf made primarily from whole wheat flour  milk, and butter. The addition of milk makes the crumb noticeably fluffier, while whole wheat provides essential fiber. It serves as a healthy and flavorful base for sandwiches, toast, and daily breakfasts.', 'abc.jpeg'),
(24, 'Butterscotch Cake for Best Dad', 'Cakes', 'None', 'kg', '425', 'A Best Dad Butterscotch Cake is a classic, nostalgic dessert beloved by traditional dads. It features a moist sponge often vanilla layered and frosted with rich butterscotch caramel cream, and generously topped with a satisfying crunch of caramelized nut praline or butterscotch chips.', 'abc.jpeg'),
(25, 'Black Forest pastry', 'Pastries', 'None', 'NOS', '17', 'A Black Forest pastry is a miniature, single-serving version of the classic German dessert originally Schwarzw lder Kirschtorte consisting of layers of chocolate cake soaked in cherry syrup, cherry filling, and fluffy whipped cream.', 'abc.jpeg');

-- --------------------------------------------------------

--
-- Table structure for table `registration`
--

CREATE TABLE `registration` (
  `id` int(11) NOT NULL,
  `FirstName` varchar(25) NOT NULL,
  `MiddleName` varchar(25) NOT NULL,
  `LastName` varchar(25) NOT NULL,
  `PhoneNo` varchar(14) NOT NULL,
  `Email` varchar(25) NOT NULL,
  `Password` varchar(10) NOT NULL,
  `Photo` text NOT NULL,
  `status` varchar(25) NOT NULL DEFAULT 'Active'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `registration`
--

INSERT INTO `registration` (`id`, `FirstName`, `MiddleName`, `LastName`, `PhoneNo`, `Email`, `Password`, `Photo`, `status`) VALUES
(1, 'Sumit', 'Rahul', 'Patil', '9373881181', 'abc@gmail.com', 'abc@1234', 'abc.jpeg', 'Block'),
(2, 'Shri', 'Wolfox', 'Wolfox', '9373881181', 'wolfox@gmail.com', '456', 'abc.jpeg', ''),
(3, 'hari', 'Rahul', 'more', '9373881181', 'hari@gmail.com', 'abc', 'abc.jpeg', ''),
(4, 'Aman', 'Aman', 'Aman', '9999999999', 'aman@gmail.com', '1234', 'abc.jpeg', ''),
(5, 'Aman', 'Aman', 'Aman', '9999999999', 'aman@gmail.com', '1234', 'abc.jpeg', 'Block'),
(6, 'Rahul', 'Rahul', 'Rahul', '119111111111', 'rahul@gmail.com', '1234', 'abc.jpeg', 'Block'),
(7, 'Rohan', 'Rohan', 'Rohan', '3333333333', 'rohan@gmail.com', '1234', 'abc.jpeg', 'Active'),
(8, 'Ashraf', 'Aslam', 'sayyad', '9090909090', 'ashrafsayyad0011@gmail.co', '1234', 'abc.jpeg', 'Active');

-- --------------------------------------------------------

--
-- Table structure for table `unit`
--

CREATE TABLE `unit` (
  `id` int(11) NOT NULL,
  `UnitName` varchar(4) NOT NULL,
  `Description` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `unit`
--

INSERT INTO `unit` (`id`, `UnitName`, `Description`) VALUES
(1, 'kg', 'KiloGram'),
(2, 'Nos', 'Numbers');

-- --------------------------------------------------------

--
-- Table structure for table `wishlist`
--

CREATE TABLE `wishlist` (
  `id` int(11) NOT NULL,
  `userid` int(11) NOT NULL,
  `productid` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `wishlist`
--

INSERT INTO `wishlist` (`id`, `userid`, `productid`) VALUES
(1, 8, 24);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `adminlogin`
--
ALTER TABLE `adminlogin`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `cart`
--
ALTER TABLE `cart`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `category`
--
ALTER TABLE `category`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `flavour`
--
ALTER TABLE `flavour`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `ordermaster`
--
ALTER TABLE `ordermaster`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `order_details`
--
ALTER TABLE `order_details`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `registration`
--
ALTER TABLE `registration`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `unit`
--
ALTER TABLE `unit`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `wishlist`
--
ALTER TABLE `wishlist`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `adminlogin`
--
ALTER TABLE `adminlogin`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `cart`
--
ALTER TABLE `cart`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `category`
--
ALTER TABLE `category`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `flavour`
--
ALTER TABLE `flavour`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `ordermaster`
--
ALTER TABLE `ordermaster`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `order_details`
--
ALTER TABLE `order_details`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `product`
--
ALTER TABLE `product`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT for table `registration`
--
ALTER TABLE `registration`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `unit`
--
ALTER TABLE `unit`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `wishlist`
--
ALTER TABLE `wishlist`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

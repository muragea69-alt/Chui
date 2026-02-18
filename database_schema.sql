-- Database schema for gas billing system

-- Table for companies
CREATE TABLE companies (
    company_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    address VARCHAR(255),
    contact_number VARCHAR(50)
);

-- Table for buyers
CREATE TABLE buyers (
    buyer_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone_number VARCHAR(50)
);

-- Table for cylinders
CREATE TABLE cylinders (
    cylinder_id INT PRIMARY KEY AUTO_INCREMENT,
    company_id INT,
    weight DECIMAL(5, 2),
    FOREIGN KEY (company_id) REFERENCES companies(company_id)
);

-- Table for transactions
CREATE TABLE transactions (
    transaction_id INT PRIMARY KEY AUTO_INCREMENT,
    buyer_id INT,
    cylinder_id INT,
    transaction_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    quantity DECIMAL(10, 2),
    total_price DECIMAL(10, 2),
    FOREIGN KEY (buyer_id) REFERENCES buyers(buyer_id),
    FOREIGN KEY (cylinder_id) REFERENCES cylinders(cylinder_id)
);
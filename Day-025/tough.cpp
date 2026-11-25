#include <iostream>
using namespace std;

// Base Class
class Grandfather {
private:
    int propertyValue; // Accessible ONLY inside Grandfather

protected:
    int propertyPassword; // Accessible in Grandfather, Father, and Son

    // Protected helper method: derived classes can use/modify this, main() cannot
    void updatePassword(int newPass) {
        propertyPassword = newPass;
    }

public:
    int propertyNumber; // Accessible everywhere (including main)

    void input() {
        cout << "--- Grandfather Details ---" << endl;
        cout << "Enter Property Value (Private): ";
        cin >> propertyValue;
        cout << "Enter Property Number (Public): ";
        cin >> propertyNumber;
        cout << "Enter Property Password (Protected): ";
        cin >> propertyPassword;
    }

    void display() {
        cout << "\n[Grandfather's Assets]" << endl;
        cout << "Property Value (Private): " << propertyValue << endl;
        cout << "Property Number (Public): " << propertyNumber << endl;
        cout << "Property Password (Protected): " << propertyPassword << endl;
    }
};

// First Derived Class (Inherits publicly from Grandfather)
class Father : public Grandfather {
private:
    int carNumber; // Accessible ONLY inside Father

protected:
    int carDocumentsID; // Accessible in Father and Son

    // Protected method to validate/modify inherited protected data
    void secureCarAndProperty() {
        // Modifying Grandfather's protected member directly
        propertyPassword += 100; 
    }

public:
    int carModelYear;

    // Overriding / Modifying base class input() behavior
    void input() {
        Grandfather::input(); // Reuse Grandfather's input logic
        
        cout << "\n--- Father Details ---" << endl;
        cout << "Enter Car Model Year (Public): ";
        cin >> carModelYear;
        cout << "Enter Car Number (Private): ";
        cin >> carNumber;
        cout << "Enter Car Documents ID (Protected): ";
        cin >> carDocumentsID;

        // Modify inherited protected state
        secureCarAndProperty();
    }

    // Overriding / Modifying base class display() behavior
    void display() {
        Grandfather::display(); // Display inherited data first
        
        cout << "\n[Father's Assets]" << endl;
        cout << "Car Model Year (Public): " << carModelYear << endl;
        cout << "Car Number (Private): " << carNumber << endl;
        cout << "Car Documents ID (Protected): " << carDocumentsID << endl;
        cout << "Updated Property Password (Modified by Father): " << propertyPassword << endl;
    }
};

// Second Derived Class (Inherits publicly from Father)
class Son : public Father {
private:
    int factoryRegNumber; // Accessible ONLY inside Son

protected:
    int factoryPassword; // Accessible inside Son (and any future subclasses)

public:
    int factoryCount;

    // Overriding / Modifying Father's input() behavior
    void input() {
        Father::input(); // Chains down to Grandfather::input() as well
        
        cout << "\n--- Son Details ---" << endl;
        cout << "Enter Number of Factories (Public): ";
        cin >> factoryCount;
        cout << "Enter Factory Reg Number (Private): ";
        cin >> factoryRegNumber;
        cout << "Enter Factory Password (Protected): ";
        cin >> factoryPassword;

        // Son can access protected members from BOTH Father and Grandfather
        carDocumentsID += 10;
        updatePassword(propertyPassword + 50); // Calling Grandfather's protected method
    }

    // Overriding / Modifying Father's display() behavior
    void display() {
        Father::display(); // Chains down to Grandfather::display()
        
        cout << "\n[Son's Assets]" << endl;
        cout << "Factory Count (Public): " << factoryCount << endl;
        cout << "Factory Reg Number (Private): " << factoryRegNumber << endl;
        cout << "Factory Password (Protected): " << factoryPassword << endl;
        cout << "Modified Car Docs ID (from Father): " << carDocumentsID << endl;
        cout << "Final Property Password (from Grandfather): " << propertyPassword << endl;
        
        // Note: Trying to access propertyValue or carNumber here would cause a compiler error
        // because they are 'private' to Grandfather and Father respectively.
    }
};

int main() {
    Son s1;

    // Public methods are accessible in main()
    s1.input();
    s1.display();

    // Demonstrating direct public access in main()
    cout << "\n--- Direct Access Check in main() ---" << endl;
    s1.propertyNumber = 999; // Allowed: public in Grandfather
    s1.carModelYear = 2025;  // Allowed: public in Father
    s1.factoryCount = 5;     // Allowed: public in Son
    cout << "Updated Public Property Number directly: " << s1.propertyNumber << endl;

    // s1.propertyValue = 5000;   // ERROR: private in Grandfather
    // s1.carDocumentsID = 123;   // ERROR: protected in Father

    return 0;
}
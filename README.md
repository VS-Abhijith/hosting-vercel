
# hosting-vercel

This project provides a simple **Flask API** that allows users to retrieve student marks based on their names from a JSON dataset. The data is stored in a file and served by the Flask application. This API can be used to query and fetch marks for specific students.

---

## 🛠️ **Technology Stack**

- **Flask**: A lightweight Python framework to build web applications.
- **Flask-CORS**: A package to handle Cross-Origin Resource Sharing (CORS) for frontend-backend communication.
- **Python 3.x**: The programming language used for the API.

---

## 📁 **Project Structure**

```
/student-marks-api
│
├── app.py                # The main Python script to run the Flask API
├── q-vercel-python.json  # The JSON file containing student data (names and marks)
├── requirements.txt      # Python dependencies for the project
├── vercel.json            # Vercel configuration for deployment
├── README.md             # This documentation file
```

---

## 📊 **Data Structure**

The student marks data is stored in a **JSON file** (`q-vercel-python.json`). It contains an array of objects where each object has the following fields:

```json
[
  {
    "name": "Student Name",
    "marks": "Marks Obtained"
  },
  ...
]
```

### Example data:
```json
{
  "name": "4",
  "marks": 32
}
```

The data represents a student where:
- `"name"`: The name or identifier of the student.
- `"marks"`: The marks obtained by the student.

---

## 🚀 **How to Run Locally**

1. **Clone the repository** (or copy the code) to your local machine.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   python app.py
   ```

4. The Flask server will start and be accessible at `http://127.0.0.1:5000`.

---

## 🌐 **Deploying on Vercel**

To deploy this project on Vercel:

1. **Create a `vercel.json` file** in your project directory with the following content:
    ```json
    {
      "version": 2,
      "builds": [
        {
          "src": "main.py",
          "use": "@vercel/python"
        }
      ],
      "routes": [
        {
          "src": "/api",
          "dest": "/main.py"
        }
      ]
    }
    ```

2. **Create a `requirements.txt` file** with the following content:
    ```
    Flask==2.0.2
    flask-cors==3.0.10
    ```

3. **Deploy** the project to Vercel using the Vercel CLI:
    ```bash
    vercel deploy
    ```

---

## 📡 **API Endpoints**

### `/api`

#### Method: `GET`

This endpoint allows you to retrieve the marks of specific students by passing their names as query parameters.

##### Request Format:

```
GET /api?name=StudentName1&name=StudentName2
```

- **Query Parameters**: You can pass one or more student names as `name` parameters.
  
##### Example Request:
```
GET http://127.0.0.1:5000/api?name=4&name=Tf3lZ0Wpf
```

##### Response Format:
The response will be a JSON object containing the marks of the requested students.

```json
{
  "marks": [32, 44]
}
```

- The `"marks"` array contains the marks corresponding to the provided student names in the same order.

---

## 🧑‍💻 **Example Use Case**

### Request:
```bash
curl "http://127.0.0.1:5000/api?name=4&name=HHxcdmfu&name=z3e7J3kd"
```

### Response:
```json
{
  "marks": [32, 48, 6]
}
```

---

## 📝 **License**

This project is licensed under the MIT License.

---

## 👨‍💻 **Contributing**

Feel free to open issues or create pull requests if you'd like to contribute to this project!

---

// Connect to MongoDB
use MongoNotes;

// Create collections

db.createCollection("users");
db.createCollection("notes");
db.createCollection("tags");

// Insert 20 users
db.users.insertMany([
    { _id: 1, name: "John Doe", password: "pass1", is_admin: false, created_at: new Date().toISOString() },
    { _id: 2, name: "Alice Smith", password: "pass2", is_admin: true, created_at: new Date().toISOString() },
    { _id: 3, name: "Bob Johnson", password: "pass3", created_at: new Date().toISOString() },
    { _id: 4, name: "Charlie Brown", password: "pass4", is_admin: false, created_at: new Date().toISOString() },
    { _id: 5, name: "Diana Prince", password: "pass5", created_at: new Date().toISOString() },
    { _id: 6, name: "Eve Adams", password: "pass6", is_admin: true, created_at: new Date().toISOString() },
    { _id: 7, name: "Frank Castle", password: "pass7", created_at: new Date().toISOString() },
    { _id: 8, name: "Grace Hopper", password: "pass8", is_admin: false, created_at: new Date().toISOString() },
    { _id: 9, name: "Henry Ford", password: "pass9", created_at: new Date().toISOString() },
    { _id: 10, name: "Ivy League", password: "pass10", created_at: new Date().toISOString() },
    { _id: 11, name: "Jack Sparrow", password: "pass11", is_admin: true, created_at: new Date().toISOString() },
    { _id: 12, name: "Karen Gillan", password: "pass12", created_at: new Date().toISOString() },
    { _id: 13, name: "Leonard Nimoy", password: "pass13", created_at: new Date().toISOString() },
    { _id: 14, name: "Mary Poppins", password: "pass14", is_admin: false, created_at: new Date().toISOString() },
    { _id: 15, name: "Nancy Drew", password: "pass15", created_at: new Date().toISOString() },
    { _id: 16, name: "Oscar Wilde", password: "pass16", created_at: new Date().toISOString() },
    { _id: 17, name: "Peter Parker", password: "pass17", is_admin: false, created_at: new Date().toISOString() },
    { _id: 18, name: "Quentin Tarantino", password: "pass18", created_at: new Date().toISOString() },
    { _id: 19, name: "Rachel Green", password: "pass19", created_at: new Date().toISOString() },
    { _id: 20, name: "Steve Rogers", password: "pass20", is_admin: true, created_at: new Date().toISOString() }
]);

// Insert 20 tags
db.tags.insertMany([
    { _id: 1, title: "Important", color: "red", created_at: new Date().toISOString() },
    { _id: 2, title: "Work", color: "blue", created_at: new Date().toISOString() },
    { _id: 3, title: "Personal", created_at: new Date().toISOString() },
    { _id: 4, title: "Urgent", color: "yellow", created_at: new Date().toISOString() },
    { _id: 5, title: "Ideas", created_at: new Date().toISOString() },
    { _id: 6, title: "Meetings", color: "green", created_at: new Date().toISOString() },
    { _id: 7, title: "Shopping", created_at: new Date().toISOString() },
    { _id: 8, title: "Health", color: "purple", created_at: new Date().toISOString() },
    { _id: 9, title: "Finance", created_at: new Date().toISOString() },
    { _id: 10, title: "Travel", color: "cyan", created_at: new Date().toISOString() },
    { _id: 11, title: "Education", created_at: new Date().toISOString() },
    { _id: 12, title: "Entertainment", color: "pink", created_at: new Date().toISOString() },
    { _id: 13, title: "Sports", created_at: new Date().toISOString() },
    { _id: 14, title: "Goals", color: "brown", created_at: new Date().toISOString() },
    { _id: 15, title: "Hobbies", created_at: new Date().toISOString() },
    { _id: 16, title: "Wishlist", color: "gray", created_at: new Date().toISOString() },
    { _id: 17, title: "Events", created_at: new Date().toISOString() },
    { _id: 18, title: "Tasks", color: "orange", created_at: new Date().toISOString() },
    { _id: 19, title: "Projects", created_at: new Date().toISOString() },
    { _id: 20, title: "Deadlines", color: "black", created_at: new Date().toISOString() }
]);

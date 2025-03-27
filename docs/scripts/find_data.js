// Use database
use MongoNotes;

// Find one
db.Users.findOne({ _id: 1 });  // Find the user with _id: 1
db.Notes.findOne({ _id: 1 });  // Find the note with _id: 1

// Find all
db.Users.find();  // Find all users
db.Notes.find();  // Find all notes

// 5 Useful finds
db.Users.find({ is_admin: true });  // Find all users who are admins
db.Notes.find({ owner_id: 1 });  // Find all notes where owner_id is 1
db.Notes.find({ created_at: { $gt: new Date('2025-01-01') } });  // Find all notes created after Jan 1, 2025
db.Notes.find({ "tags.title": "Technology" });  // Find all notes with the "Technology" tag
db.Notes.find({ status: "completed" });  // Find all notes where status is "completed"

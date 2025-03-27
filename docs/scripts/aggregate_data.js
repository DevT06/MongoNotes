// Use database
use MongoNotes;

// User
db.User.countDocuments();
db.User.countDocuments({ is_admin: true });

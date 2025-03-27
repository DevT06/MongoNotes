// Use database
use MongoNotes;

// User
db.Users.deleteOne(
  { _id: 2 }  // Delete the user with _id: 2
);

// Note
db.Notes.deleteOne(
  { _id: 3 }  // Delete the note with _id: 3
);

// Tag (even though not tecnically deleted just updated Note)
db.Notes.updateOne(
  { _id: 1 },  // Find the note with _id: 1
  {
    $pull: {
      tags: { _id: 1 }  // Remove the tag with _id: 1 from the tags array
    }
  }
);

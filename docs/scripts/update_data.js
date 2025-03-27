// Use database
use MongoNotes;

// User
db.Users.updateOne(
  { _id: 1 },  // Find the user with _id: 1
  {
    $set: {
      name: "John Doe Updated",  // Modify the name
      password: "newpassword123",  // Modify the password
      last_login: new Date(),  // Add the new optional attribute: last_login
      email: "john.doe@example.com"  // Add the new optional attribute: email
    },
    $unset: {
      created_at: ""  // Remove the created_at attribute (optional)
    }
  }
);

// Note
db.Notes.updateOne(
  { _id: 1 },  // Find the note with _id: 1
  {
    $set: {
      title: "Updated Tech Innovations",  // Modify the title
      content: "Updated content for the article",  // Modify the content
      updated_at: new Date(),  // Add the new optional attribute: updated_at
      weight: 3  // Add the new optional attribute: weight
    },
    $unset: {
      status: "",  // Remove the status attribute (optional)
      tags: ""  // Remove the tags attribute (optional)
    }
  }
);

// Tag
db.Notes.updateOne(
  { _id: 1 },  // Find the note with _id: 1
  {
    $set: {
      "tags[0].description": "Updated description for tech-related articles",  // Modify the description
      "tags[0].color": "purple",  // Modify the color
      "tags[0].created_at": new Date()  // Add the new optional attribute: created_at
    },
    $unset: {
      "tags.0.weight": ""  // Remove the weight attribute from the tag (optional)
    }
  }
);

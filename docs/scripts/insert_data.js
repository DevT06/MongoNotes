// Use database
use MongoNotes;

// Users
db.Users.insertMany([
  { _id: 1, name: "John Doe", password: "password123", is_admin: true, created_at: new Date() },
  { _id: 2, name: "Jane Smith", password: "securepass456" },
  { _id: 3, name: "Robert Johnson", password: "password789", is_admin: true },
  { _id: 4, name: "Emily Davis", password: "mypassword012", created_at: new Date() },
  { _id: 5, name: "Michael Brown", password: "admin1234" },
  { _id: 6, name: "Linda Wilson", password: "mypassword567", created_at: new Date() },
  { _id: 7, name: "William Moore", password: "1234password" },
  { _id: 8, name: "Sophia Taylor", password: "securepass987", is_admin: true },
  { _id: 9, name: "James Anderson", password: "anderson123" },
  { _id: 10, name: "Olivia Thomas", password: "123securepass", created_at: new Date() },
  { _id: 11, name: "David Jackson", password: "jackson567" },
  { _id: 12, name: "Ava White", password: "ava1234", created_at: new Date() },
  { _id: 13, name: "Ethan Harris", password: "harris5678" },
  { _id: 14, name: "Mason Martin", password: "masonpass234", is_admin: true },
  { _id: 15, name: "Isabella Thompson", password: "isabella001" },
  { _id: 16, name: "Mia Garcia", password: "miapass123", created_at: new Date() },
  { _id: 17, name: "Benjamin Martinez", password: "benjamin321" },
  { _id: 18, name: "Charlotte Robinson", password: "charlotte654", created_at: new Date() },
  { _id: 19, name: "Lucas Clark", password: "lucas987" },
  { _id: 20, name: "Amelia Rodriguez", password: "amelia234" }
]);

// Notes (including Tags)
db.Notes.insertMany([
  { _id: 1, title: "Tech Innovations", owner_id: 1, content: "Exploring the latest in technology.", created_at: new Date(), tags: [
      { _id: 1, title: "Technology", description: "Articles about tech", color: "blue", created_at: new Date() }
    ]
  },
  { _id: 2, title: "Healthy Lifestyle Tips", owner_id: 2, tags: [
      { _id: 5, title: "Health" }
    ]
  },
  { _id: 3, title: "Science Experiments", owner_id: 3, content: "Fun and easy experiments for kids.", created_at: new Date(), tags: [
      { _id: 3, title: "Science", description: "Scientific studies", created_at: new Date() }
    ]
  },
  { _id: 4, title: "Investment Strategies", owner_id: 4, tags: [
      { _id: 4, title: "Finance", description: "Investment advice" }
    ]
  },
  { _id: 5, title: "Top Travel Destinations", owner_id: 5, content: "Top places to visit this summer.", tags: [
      { _id: 6, title: "Travel", description: "Travel destinations and guides", color: "green", created_at: new Date() }
    ]
  },
  { _id: 6, title: "Best Foods for Health", owner_id: 6, created_at: new Date(), tags: [
      { _id: 5, title: "Health", description: "Healthy living tips" }
    ]
  },
  { _id: 7, title: "Top Movies of 2025", owner_id: 7, content: "A list of the most anticipated movies of the year.", tags: [
      { _id: 8, title: "Entertainment", created_at: new Date() }
    ]
  },
  { _id: 8, title: "How to Play Guitar", owner_id: 8, tags: [
      { _id: 9, title: "Music", created_at: new Date() }
    ]
  },
  { _id: 9, title: "Fitness Plan", owner_id: 9, content: "An easy fitness plan to follow.", created_at: new Date(), tags: [
      { _id: 7, title: "Fitness", description: "Fitness and health", created_at: new Date() }
    ]
  },
  { _id: 10, title: "Political Debate", owner_id: 10, status: "pending", tags: [
      { _id: 13, title: "Politics", description: "Political discussions", created_at: new Date() }
    ]
  },
  { _id: 11, title: "Art in the 21st Century", owner_id: 1, content: "Exploring modern art", created_at: new Date(), tags: [
      { _id: 10, title: "Art", description: "Visual art", color: "red", created_at: new Date() }
    ]
  },
  { _id: 12, title: "Music Festivals", owner_id: 2, content: "Top music festivals to attend this year.", created_at: new Date(), tags: [
      { _id: 9, title: "Music", description: "Music genres and artists" }
    ]
  },
  { _id: 13, title: "How to Train Dogs", owner_id: 3, weight: 2, tags: [
      { _id: 7, title: "Pets", description: "Animal care", created_at: new Date() }
    ]
  },
  { _id: 14, title: "History of World War II", owner_id: 4, content: "A brief overview of World War II.", updated_at: new Date(), tags: [
      { _id: 14, title: "History", created_at: new Date() }
    ]
  },
  { _id: 15, title: "Economic Growth in 2025", owner_id: 5, tags: [
      { _id: 15, title: "Economy", description: "Global economy trends" }
    ]
  },
  { _id: 16, title: "DIY Home Decor", owner_id: 6, status: "completed", created_at: new Date(), tags: [
      { _id: 18, title: "DIY", description: "Do-it-yourself projects", color: "brown" }
    ]
  },
  { _id: 17, title: "Fitness Motivation", owner_id: 7, content: "How to stay motivated for workouts.", created_at: new Date(), tags: [
      { _id: 7, title: "Fitness", description: "Fitness and health", created_at: new Date() }
    ]
  },
  { _id: 18, title: "Pets and Their Care", owner_id: 8, content: "Understanding your pet’s needs.", created_at: new Date(), tags: [
      { _id: 7, title: "Pets", description: "Animal care" }
    ]
  },
  { _id: 19, title: "Politics in 2025", owner_id: 9, weight: 5, tags: [
      { _id: 13, title: "Politics", description: "Political discussions", created_at: new Date() }
    ]
  },
  { _id: 20, title: "Fitness for Beginners", owner_id: 10, content: "Basic fitness plan for newcomers.", tags: [
      { _id: 7, title: "Fitness", description: "Fitness and health" }
    ]
  }
]);

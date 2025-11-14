import json
import random
import re
from datetime import datetime

class AICSChatbot:
    def __init__(self):
        self.name = "AI-CS Assistant"
        self.version = "1.0"
        self.knowledge_base = self.load_knowledge_base()
        
    def load_knowledge_base(self):
        """Load AI and CS domain knowledge base"""
        return {
            # Artificial Intelligence Topics
            "machine learning": {
                "definition": "Machine Learning is a subset of AI that enables systems to learn and improve from experience without being explicitly programmed.",
                "types": ["Supervised Learning", "Unsupervised Learning", "Reinforcement Learning", "Semi-supervised Learning"],
                "applications": ["Image Recognition", "Natural Language Processing", "Recommendation Systems", "Predictive Analytics"]
            },
            "deep learning": {
                "definition": "Deep Learning is a subset of machine learning based on artificial neural networks with multiple layers.",
                "key_concepts": ["Neural Networks", "Backpropagation", "CNNs", "RNNs", "Transformers"],
                "frameworks": ["TensorFlow", "PyTorch", "Keras", "JAX"]
            },
            "neural network": {
                "definition": "A neural network is a computing system inspired by biological neural networks that learns to perform tasks by considering examples.",
                "components": ["Input Layer", "Hidden Layers", "Output Layer", "Weights", "Biases", "Activation Functions"],
                "types": ["Feedforward NN", "Convolutional NN", "Recurrent NN", "Transformer"]
            },
            "nlp": {
                "definition": "Natural Language Processing (NLP) is a branch of AI that helps computers understand, interpret and manipulate human language.",
                "tasks": ["Sentiment Analysis", "Named Entity Recognition", "Machine Translation", "Text Summarization", "Question Answering"],
                "models": ["BERT", "GPT", "T5", "RoBERTa"]
            },
            # Computer Science Topics
            "algorithm": {
                "definition": "An algorithm is a step-by-step procedure or formula for solving a problem or completing a task.",
                "complexity": ["Time Complexity", "Space Complexity", "Big O Notation"],
                "types": ["Sorting", "Searching", "Graph Algorithms", "Dynamic Programming", "Greedy Algorithms"]
            },
            "data structure": {
                "definition": "A data structure is a specialized format for organizing, processing, retrieving and storing data.",
                "types": ["Array", "Linked List", "Stack", "Queue", "Tree", "Graph", "Hash Table", "Heap"],
                "operations": ["Insertion", "Deletion", "Search", "Traversal"]
            },
            "database": {
                "definition": "A database is an organized collection of structured information or data stored electronically.",
                "types": ["Relational (SQL)", "NoSQL", "Graph", "Document-based", "Key-Value"],
                "concepts": ["ACID Properties", "Normalization", "Indexing", "Query Optimization"]
            },
            "operating system": {
                "definition": "An Operating System is system software that manages computer hardware and software resources.",
                "functions": ["Process Management", "Memory Management", "File System", "I/O Management", "Security"],
                "examples": ["Linux", "Windows", "macOS", "Unix"]
            },
            "programming": {
                "definition": "Programming is the process of creating a set of instructions that tell a computer how to perform a task.",
                "paradigms": ["Object-Oriented", "Functional", "Procedural", "Declarative"],
                "languages": ["Python", "Java", "C++", "JavaScript", "Go", "Rust"]
            },
            "cloud computing": {
                "definition": "Cloud computing is the delivery of computing services over the internet.",
                "models": ["IaaS", "PaaS", "SaaS"],
                "providers": ["AWS", "Google Cloud", "Microsoft Azure", "IBM Cloud"]
            }
        }
    
    def normalize_query(self, query):
        """Normalize user query for better matching"""
        return query.lower().strip()
    
    def find_relevant_topic(self, query):
        """Find the most relevant topic from knowledge base"""
        query_normalized = self.normalize_query(query)
        
        # Check for exact matches first
        for topic in self.knowledge_base:
            if topic in query_normalized:
                return topic
        
        # Check for partial matches
        keywords = {
            "ml": "machine learning",
            "nn": "neural network",
            "ai": "machine learning",
            "natural language": "nlp",
            "os": "operating system",
            "db": "database",
            "ds": "data structure",
            "algo": "algorithm"
        }
        
        for keyword, topic in keywords.items():
            if keyword in query_normalized:
                return topic
        
        return None
    
    def generate_response(self, query):
        """Generate response based on user query"""
        topic = self.find_relevant_topic(query)
        
        if topic:
            info = self.knowledge_base[topic]
            response = f"\n📚 Topic: {topic.upper()}\n\n"
            response += f"Definition: {info['definition']}\n"
            
            # Add additional relevant information
            for key, value in info.items():
                if key != 'definition' and isinstance(value, list):
                    response += f"\n{key.replace('_', ' ').title()}:\n"
                    for item in value:
                        response += f"  • {item}\n"
            
            return response
        else:
            return self.handle_unknown_query(query)
    
    def handle_unknown_query(self, query):
        """Handle queries not in knowledge base"""
        suggestions = [
            "I specialize in AI and Computer Science topics. Try asking about:",
            "  • Machine Learning",
            "  • Deep Learning",
            "  • Neural Networks",
            "  • Natural Language Processing (NLP)",
            "  • Algorithms",
            "  • Data Structures",
            "  • Databases",
            "  • Operating Systems",
            "  • Programming",
            "  • Cloud Computing"
        ]
        return "\n".join(suggestions)
    
    def run(self):
        """Run the chatbot"""
        print(f"\n{'='*60}")
        print(f"  Welcome to {self.name} v{self.version}")
        print(f"  Your AI & Computer Science Knowledge Assistant")
        print(f"{'='*60}\n")
        print("Type 'exit', 'quit', or 'bye' to end the conversation.\n")
        
        while True:
            try:
                user_input = input("You: ").strip()
                
                if not user_input:
                    continue
                
                # Check for exit commands
                if user_input.lower() in ['exit', 'quit', 'bye', 'goodbye']:
                    print(f"\n{self.name}: Thank you for using AI-CS Assistant! Goodbye! 👋\n")
                    break
                
                # Check for help command
                if user_input.lower() in ['help', '?']:
                    print(f"\n{self.name}:")
                    print(self.handle_unknown_query(""))
                    print()
                    continue
                
                # Generate and display response
                response = self.generate_response(user_input)
                print(f"\n{self.name}: {response}\n")
                
            except KeyboardInterrupt:
                print(f"\n\n{self.name}: Goodbye! 👋\n")
                break
            except Exception as e:
                print(f"\n{self.name}: An error occurred: {str(e)}\n")

if __name__ == "__main__":
    chatbot = AICSChatbot()
    chatbot.run()

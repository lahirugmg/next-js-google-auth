import TransactionForm from '@/components/TransactionForm';
import LoginButton from '@/components/LoginButton';

export default function Home() {
  return (
    <div className="min-h-screen bg-gray-50 py-8">
      <div className="container mx-auto px-4">
        <div className="text-center mb-8">
          <h1 className="text-4xl font-bold text-gray-900 mb-2">
            Business Expense Tracker
          </h1>
          <p className="text-gray-600 mb-6">
            Track your business expenses and income
          </p>
          
          <div className="flex justify-center mb-8">
            <LoginButton />
          </div>
        </div>
        
        <TransactionForm />
      </div>
    </div>
  );
}

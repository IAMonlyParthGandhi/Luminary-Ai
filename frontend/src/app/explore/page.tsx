import Chatbot from '@/components/chat/ChatbotSmall'
import CompanyInput from '@/components/company/CompanyInput'
import Navbar from '@/components/layout/Navbar'
import React from 'react'

const page = () => {
  return (
    <div className='items-center justify-center'>
    <Navbar />
      <CompanyInput />
      <Chatbot />
    </div>
  )
}

export default page

'use client'
import Contact from '@/components/contact/ContactUs'
import Footer from '@/components/layout/Footer'
import Navbar from '@/components/layout/Navbar'
import React from 'react'

const page = () => {
  return (
    <div className=''>
      <Navbar />
      <Contact />
      <Footer />
    </div>
  )
}

export default page

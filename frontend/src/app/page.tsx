import Footer from "@/components/layout/Footer";
import Hero from "@/components/home/Hero";
import Navbar from "@/components/layout/Navbar";
import Work from "@/components/home/Work";
import BrandLogos from "@/components/home/Sponsors";

export default function Home() {
  return (
    <div className="bg-level-1">
      <Navbar />
      <Hero />
      <Work />
      <BrandLogos />
      <Footer />
    </div>
  );
}
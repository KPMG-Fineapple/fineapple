import Grid from "@mui/material/Grid";
import MainFeaturedPost from "src/components/home/main-post";
import FeaturedPost from "src/components/home/feature-post";
import { Layout } from "src/components/home/layout";

function Main() {
  const mainFeaturedPost = {
    title: "fineapple과 함께 에너지에 투자해보세요",
    description: "한번의 소중한 투자로 환경도 살리고, 수익도 챙기고!",
    image:
      "https://newsimg-hams.hankookilbo.com/2022/02/03/4b4eff73-5adb-40a2-99a3-bf4aa929fa3e.jpg",
    imageText: "main image description",
  };

  const featuredPosts = [
    {
      title: "HOME-Solar (가정용 태양광 올인원 서비스)",
      description: "우리 집에 가정용 태양광 패널 설치하러 가기",
      image:
        "http://www.solartodaymag.com/news/photo/201706/4574_3285_4224.jpg",
      imageText: "Image Text",
      url: "/home/main?mode=dashboard",
    },
    {
      title: "INVEST-Solar (대규모 태양광 발전소 투자 펀딩 플랫폼)",
      description: "소액으로 태양광 발전소에 투자하러 가기",
      image:
        "https://img.etoday.co.kr/pto_db/2019/01/600/20190121101335_1293391_1200_800.jpg",
      imageText: "Image Text",
      url: "/home/main?mode=invest",
    },
  ];

  return (
    <Layout>
      <MainFeaturedPost post={mainFeaturedPost} />
      <Grid container spacing={4}>
        {featuredPosts.map((post) => (
          <FeaturedPost key={post.title} post={post} />
        ))}
      </Grid>
    </Layout>
  );
}

export default Main;

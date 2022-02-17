import Grid from "@mui/material/Grid";
import MainFeaturedPost from "src/components/home/main-post";
import FeaturedPost from "src/components/home/feature-post";
import { Layout } from "src/components/home/layout";

function Main() {
  const mainFeaturedPost = {
    title: "Fine apple의 태양광 솔루션",
    description:
      "소개문구 써주세요 소개문구 써주세요 소개문구 써주세요 소개문구 써주세요 소개문구 써주세요 소개문구 써주세요소개문구 써주세요 소개문구 써주세요 소개문구 써주세요 소개문구 써주세요",
    image:
      "https://newsimg-hams.hankookilbo.com/2022/02/03/4b4eff73-5adb-40a2-99a3-bf4aa929fa3e.jpg",
    imageText: "main image description",
  };

  const featuredPosts = [
    {
      title: "태양광 올인원 서비스",
      description:
        "소개문구 써주세요 소개문구 써주세요 소개문구 써주세요 소개문구 써주세요 소개문구 써주세요 소개문구 써주세요 소개문구 써주세요 소개문구 써주세요 소개문구 써주세요 소개문구 써주세요",
      image:
        "http://www.solartodaymag.com/news/photo/201706/4574_3285_4224.jpg",
      imageText: "Image Text",
      url: "/home/main?mode=dashboard",
    },
    {
      title: "태양광 투자 서비스",
      description:
        "소개문구 써주세요 소개문구 써주세요 소개문구 써주세요 소개문구 써주세요 소개문구 써주세요 소개문구 써주세요 소개문구 써주세요 소개문구 써주세요 소개문구 써주세요 소개문구 써주세요",
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

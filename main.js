import { Client } from "discord.js-selfbot-v13";
import { Streamer,streamLivestreamVideo } from '@dank074/discord-video-stream';

const streamer = new Streamer(new Client());
await streamer.client.login(process.env.botToken);
await streamer.joinVoice("1122707918177960047", "1200346808552001538");

const udp = await streamer.createStream({
    // stream options here
});
udp.mediaConnection.setSpeaking(true);
udp.mediaConnection.setVideoStatus(true);
try {
    const res = await streamLivestreamVideo("https://fo-hlc.tv360.vn/bpk-tv/192/output/index.m3u8?auth=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJtZXRob2QiOiJHRVQiLCJleHAiOjE3MTc1NzY5MTcsInVyaSI6Ii9icGstdHYvMTkyL291dHB1dC9pbmRleC5tM3U4In0.A9euuf8tZqFGtxdnwqi-k7xDblCbKQLpeGhUoKzn1IA", udp);

    console.log("Finished playing video " + res);
} catch (e) {
    console.log(e);
} finally {
    udp.mediaConnection.setSpeaking(false);
    udp.mediaConnection.setVideoStatus(false);
}
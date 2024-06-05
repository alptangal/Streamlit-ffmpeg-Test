import { Client } from "discord.js-selfbot-v13";
import { Streamer,streamLivestreamVideo } from '@dank074/discord-video-stream';

const streamer = new Streamer(new Client());
await streamer.client.login(process.env.botToken);
await streamer.joinVoice("1122707918177960047", "1200346808552001538");

const udp = await streamer.createStream({
    // stream options here
    //h26xPreset: 'ultrafast',
   // rtcpSenderReportEnabled: true,
    //fps: 720,
    hardwareAcceleratedDecoding: true,
    fps:24
});
udp.mediaConnection.setSpeaking(true);
udp.mediaConnection.setVideoStatus(true);
try {
    const res = await streamLivestreamVideo("https://fo-hlc.tv360.vn/bpk-tv/249/output/index.m3u8?auth=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJtZXRob2QiOiJHRVQiLCJleHAiOjE3MTc1OTg1OTIsInVyaSI6Ii9icGstdHYvMjQ5L291dHB1dC9pbmRleC5tM3U4In0.X_JjDLGH_rrHIjcpLmlNDsTUOg3M7qNUAgSqoMdir7U&manifestfilter=video_bitrate:1-5767168", udp);

    console.log("Finished playing video " + res);
} catch (e) {
    console.log(e);
} finally {
    udp.mediaConnection.setSpeaking(false);
    udp.mediaConnection.setVideoStatus(false);
}
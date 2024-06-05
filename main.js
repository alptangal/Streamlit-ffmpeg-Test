import { Client } from "discord.js-selfbot-v13";
import { Streamer,streamLivestreamVideo } from '@dank074/discord-video-stream';

const streamer = new Streamer(new Client());
await streamer.client.login(process.env.botToken);
await streamer.joinVoice("1122707918177960047", "1200346808552001538");

const udp = await streamer.createStream({
    // stream options here
    //h26xPreset: 'ultrafast',
    rtcpSenderReportEnabled: true,
    //fps: 720,
    hardwareAcceleratedDecoding: true
});
udp.mediaConnection.setSpeaking(true);
udp.mediaConnection.setVideoStatus(true);
try {
    const res = await streamLivestreamVideo("https://tr-netcdn.tv360.vn/netcdn-live/155/output/index.m3u8?timestamp=1717595742&token=8f98b7016816be8b9c2388c37df59ef8", udp);

    console.log("Finished playing video " + res);
} catch (e) {
    console.log(e);
} finally {
    udp.mediaConnection.setSpeaking(false);
    udp.mediaConnection.setVideoStatus(false);
}